"""Single-GPU supervised causal training with assistant-only loss."""
import json
from pathlib import Path
from .data import read_rows
from .prompts import messages

def encode_example(tokenizer, row, max_length=768):
    prompt = tokenizer.apply_chat_template(messages(row["text"]), tokenize=False, add_generation_prompt=True)
    # Qwen chat template renders the same prefix followed by assistant response/end token.
    full = tokenizer.apply_chat_template(messages(row["text"]) + [{"role": "assistant", "content": json.dumps(row["target"], sort_keys=True)}], tokenize=False)
    ids = tokenizer(full, add_special_tokens=False)["input_ids"]
    prefix = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    if ids[:len(prefix)] != prefix:
        raise ValueError("Chat template prefix mismatch; inspect template before training")
    if len(ids) > max_length:
        raise ValueError("Example exceeds max_length: do not silently truncate targets")
    labels = [-100] * len(prefix) + ids[len(prefix):]
    if all(x == -100 for x in labels):
        raise ValueError("No supervised assistant tokens")
    return {"input_ids": ids, "attention_mask": [1] * len(ids), "labels": labels}

def train(config_path):
    import torch
    from datasets import Dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Trainer, TrainingArguments, set_seed
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    config = json.loads(Path(config_path).read_text())
    if not torch.cuda.is_available():
        raise RuntimeError("Training profile requires one CUDA GPU; CPU baseline remains available")
    set_seed(config["seed"])
    model_path = config["model_path"]
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, trust_remote_code=False)
    tokenizer.pad_token = tokenizer.eos_token
    kwargs = dict(local_files_only=True, trust_remote_code=False, torch_dtype=torch.float16, device_map={"": 0})
    if config["method"] == "qlora":
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.float16)
    elif config["method"] != "lora":
        raise ValueError("method must be lora or qlora")
    model = AutoModelForCausalLM.from_pretrained(model_path, **kwargs)
    model.config.use_cache = False
    if config["method"] == "qlora":
        model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, LoraConfig(task_type="CAUSAL_LM", r=config["rank"], lora_alpha=config["alpha"],
        lora_dropout=0.05, target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], bias="none"))
    model.enable_input_require_grads()
    train_rows, val_rows = read_rows(config["train_file"]), read_rows(config["validation_file"])
    if {r["template_family"] for r in train_rows} & {r["template_family"] for r in val_rows}:
        raise ValueError("Template leakage between training and validation")
    datasets = [Dataset.from_list([encode_example(tokenizer, row, config["max_length"]) for row in rows]) for rows in (train_rows, val_rows)]
    def collate(rows):
        width = max(len(r["input_ids"]) for r in rows)
        return {key: torch.tensor([r[key] + [(-100 if key == "labels" else tokenizer.pad_token_id if key == "input_ids" else 0)] * (width-len(r[key])) for r in rows]) for key in ("input_ids", "attention_mask", "labels")}
    args = TrainingArguments(output_dir=config["output_dir"], seed=config["seed"], num_train_epochs=config["epochs"],
        per_device_train_batch_size=1, per_device_eval_batch_size=1, gradient_accumulation_steps=8,
        learning_rate=config["learning_rate"], fp16=True, gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False}, eval_strategy="epoch", save_strategy="epoch",
        save_total_limit=2, logging_steps=10, report_to="none")
    trainer = Trainer(model=model, args=args, train_dataset=datasets[0], eval_dataset=datasets[1], data_collator=collate)
    trainer.train()
    model.save_pretrained(config["output_dir"], safe_serialization=True)
    tokenizer.save_pretrained(config["output_dir"])
    Path(config["output_dir"], "run-config.json").write_text(json.dumps(config, indent=2))
    return trainer.evaluate()

def merge(base, adapter, output):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel
    # Merge into fresh FP16 base, never directly into NF4 training weights.
    model = AutoModelForCausalLM.from_pretrained(base, local_files_only=True, torch_dtype=torch.float16, device_map="auto", trust_remote_code=False)
    model = PeftModel.from_pretrained(model, adapter, local_files_only=True).merge_and_unload()
    model.save_pretrained(output, safe_serialization=True)
    AutoTokenizer.from_pretrained(base, local_files_only=True).save_pretrained(output)

def quantize(model_path, output):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    if not torch.cuda.is_available():
        raise RuntimeError("NF4 quantization profile requires CUDA")
    model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True, trust_remote_code=False, device_map="auto",
        quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.float16))
    model.save_pretrained(output, safe_serialization=True)
    AutoTokenizer.from_pretrained(model_path, local_files_only=True).save_pretrained(output)
    return {"method": "bitsandbytes-nf4", "model_memory_bytes": model.get_memory_footprint()}
