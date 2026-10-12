"""Local HF or private OpenAI-compatible vLLM; no hosted LLM API defaults."""
import os
from .prompts import messages

class VLLMClient:
    def __init__(self, url="http://127.0.0.1:8001/v1", model="portshield", timeout=60):
        import httpx
        self.url, self.model = url.rstrip("/"), model
        self.client = httpx.Client(timeout=timeout, trust_env=False)

    def complete_messages(self, items, max_tokens=256):
        key = os.getenv("VLLM_API_KEY", "")
        response = self.client.post(self.url + "/chat/completions",
            headers={"Authorization": "Bearer " + key}, json={"model": self.model, "messages": items,
            "temperature": 0, "max_tokens": max_tokens})
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def predict(self, text):
        return self.complete_messages(messages(text))

    def close(self):
        self.client.close()

class HFClient:
    def __init__(self, model, adapter=None, four_bit=False):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        self.torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(model, local_files_only=True, trust_remote_code=False)
        kwargs = {"local_files_only": True, "trust_remote_code": False, "device_map": "auto", "torch_dtype": torch.float16 if torch.cuda.is_available() else torch.float32}
        if four_bit:
            if not torch.cuda.is_available():
                raise RuntimeError("NF4 workflow requires CUDA")
            kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.float16)
        self.model = AutoModelForCausalLM.from_pretrained(model, **kwargs)
        if adapter:
            from peft import PeftModel
            self.model = PeftModel.from_pretrained(self.model, adapter, local_files_only=True)
        self.model.eval()

    def predict(self, text):
        batch = self.tokenizer.apply_chat_template(messages(text), tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(self.model.device)
        with self.torch.inference_mode():
            output = self.model.generate(**batch, max_new_tokens=256, do_sample=False, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(output[0, batch["input_ids"].shape[1]:], skip_special_tokens=True)
