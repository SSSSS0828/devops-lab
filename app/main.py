from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def index():
    return {
        "service": "devops-lab",
        "status": "ok",
        "version": "v3"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
