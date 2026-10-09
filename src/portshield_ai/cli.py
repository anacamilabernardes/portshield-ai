import argparse
import asyncio
import json
from .data import generate, read_rows
from .baseline import classify
from .evaluation import evaluate

def main():
    p = argparse.ArgumentParser(description="PortShield public/synthetic research workflows")
    sub = p.add_subparsers(dest="command", required=True)
    g = sub.add_parser("generate"); g.add_argument("--out",default="data/synthetic"); g.add_argument("--per-class", type=int, default=40); g.add_argument("--seed", type=int, default=42)
    c = sub.add_parser("classify"); c.add_argument("text")
    e = sub.add_parser("evaluate"); e.add_argument("--data",default="data/synthetic/test.jsonl"); e.add_argument("--out",default="results/runs/evaluation.json"); e.add_argument("--backend",choices=["baseline","vllm","hf"],default="baseline"); e.add_argument("--model",default="models/base"); e.add_argument("--adapter"); e.add_argument("--four-bit",action="store_true"); e.add_argument("--url",default="http://127.0.0.1:8001/v1"); e.add_argument("--served-model",default="portshield"); e.add_argument("--mlflow",action="store_true")
    t = sub.add_parser("train"); t.add_argument("--config",default="configs/qlora.json")
    m = sub.add_parser("merge"); m.add_argument("--base",default="models/base"); m.add_argument("--adapter",default="models/adapter"); m.add_argument("--out",default="models/merged")
    q = sub.add_parser("quantize"); q.add_argument("--model",default="models/merged"); q.add_argument("--out",default="models/nf4")
    r = sub.add_parser("rag"); r.add_argument("question"); r.add_argument("--corpus",default="data/public/corpus.json"); r.add_argument("--generative",action="store_true"); r.add_argument("--url",default="http://127.0.0.1:8001/v1")
    re = sub.add_parser("rag-evaluate"); re.add_argument("--cases", default="data/public/rag-cases.json"); re.add_argument("--corpus",default="data/public/corpus.json"); re.add_argument("--out",default="results/runs/rag-evaluation.json"); re.add_argument("--generative",action="store_true"); re.add_argument("--url",default="http://127.0.0.1:8001/v1")
    b = sub.add_parser("benchmark"); b.add_argument("--data",default="data/synthetic/test.jsonl"); b.add_argument("--url",default="http://127.0.0.1:8001/v1"); b.add_argument("--model",default="portshield"); b.add_argument("--concurrency",type=int,default=1); b.add_argument("--limit",type=int,default=30); b.add_argument("--out",default="results/runs/benchmark.json"); b.add_argument("--gpu-memory-file")
    i = sub.add_parser("ingest"); i.add_argument("--text",required=True); i.add_argument("--metadata",required=True); i.add_argument("--corpus",default="data/public/corpus.json")
    args = p.parse_args()
    client = None
    try:
        if args.command == "generate":
            result = generate(args.out, args.per_class,args.seed)
        elif args.command == "classify":
            result = classify(args.text).model_dump()
        elif args.command == "evaluate":
            predictor = lambda text: classify(text).model_dump_json()
            if args.backend != "baseline":
                from .inference import HFClient, VLLMClient
                client = VLLMClient(args.url,args.served_model) if args.backend == "vllm" else HFClient(args.model,args.adapter,args.four_bit)
                predictor = client.predict
            result = evaluate(args.data,predictor,args.out,args.mlflow)
        elif args.command == "train":
            from .training import train
            result = train(args.config)
        elif args.command == "merge":
            from .training import merge
            merge(args.base,args.adapter,args.out); result = {"output":args.out}
        elif args.command == "quantize":
            from .training import quantize
            result = quantize(args.model,args.out)
        elif args.command == "rag":
            from .rag import load_corpus, answer
            if args.generative:
                from .inference import VLLMClient
                client = VLLMClient(args.url)
            result = answer(args.question,load_corpus(args.corpus),["analyst"],client)
        elif args.command == "rag-evaluate":
            from .rag_evaluation import evaluate_rag
            if args.generative:
                from .inference import VLLMClient
                client = VLLMClient(args.url)
            result = evaluate_rag(args.cases,args.corpus,args.out,client)
        elif args.command == "ingest":
            from .rag import ingest
            ingest(args.text,args.metadata,args.corpus); result = {"status":"imported"}
        else:
            from .benchmark import benchmark
            prompts = [r["text"] for r in read_rows(args.data)[:args.limit]]
            result = asyncio.run(benchmark(args.url,args.model,prompts,args.out,args.concurrency,gpu_memory_file=args.gpu_memory_file))
        print(json.dumps(result,indent=2))
    finally:
        if client and hasattr(client,"close"):
            client.close()

if __name__ == "__main__":
    main()
