import os
import time
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from .auth import principal
from .baseline import classify, abstain
from .schema import ReportRequest, QueryRequest, EventAnalysis
from .rag import load_corpus, answer
from .inference import VLLMClient

REQUESTS = Counter("portshield_requests_total", "Authenticated completed tasks", ["task", "status"])
LATENCY = Histogram("portshield_task_seconds", "Task duration", ["task"])

@asynccontextmanager
async def lifespan(app):
    app.state.corpus = load_corpus(os.getenv("CORPUS_PATH", "data/public/corpus.json"))
    backend = os.getenv("MODEL_BACKEND", "baseline")
    if backend not in {"baseline", "vllm"}:
        raise RuntimeError("Unknown MODEL_BACKEND")
    app.state.client = VLLMClient(os.getenv("VLLM_URL", "http://127.0.0.1:8001/v1")) if backend == "vllm" else None
    yield
    if app.state.client:
        app.state.client.close()

app = FastAPI(title="PortShield AI", version="0.1.0", lifespan=lifespan)

@app.get("/healthz")
def health():
    return {"status": "alive"}

@app.get("/readyz")
def ready():
    if not hasattr(app.state, "corpus"):
        raise HTTPException(503, "Corpus unavailable")
    if app.state.client:
        try:
            r = app.state.client.client.get(app.state.client.url + "/models", headers={"Authorization": "Bearer " + os.getenv("VLLM_API_KEY", "")})
            r.raise_for_status()
        except Exception:
            raise HTTPException(503, "Inference unavailable") from None
    return {"status": "ready"}

@app.post("/v1/events/analyze", response_model=EventAnalysis)
def analyze(body: ReportRequest, user=Depends(principal)):
    start = time.perf_counter()
    try:
        result = EventAnalysis.model_validate_json(app.state.client.predict(body.text)) if app.state.client else classify(body.text)
    except ValueError:
        result = abstain()
    except Exception:
        REQUESTS.labels("classify", "error").inc()
        raise HTTPException(503, "Inference unavailable") from None
    LATENCY.labels("classify").observe(time.perf_counter()-start)
    REQUESTS.labels("classify", "abstain" if result.event_type == "unknown" else "ok").inc()
    return result

@app.post("/v1/rag/query")
def query(body: QueryRequest, user=Depends(principal)):
    start = time.perf_counter()
    try:
        result = answer(body.question, app.state.corpus, user["roles"], app.state.client)
    except Exception:
        REQUESTS.labels("rag", "error").inc()
        raise HTTPException(503, "Inference unavailable") from None
    LATENCY.labels("rag").observe(time.perf_counter()-start)
    REQUESTS.labels("rag", "abstain" if result["abstained"] else "ok").inc()
    return result

@app.get("/metrics")
def metrics(user=Depends(principal)):
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
