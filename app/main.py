import os

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# 如果系统提供了 APP_ENV 环境变量，则使用它的值，否则默认为 development
APP_ENV = os.getenv("APP_ENV", "development")

@app.get("/")
def index():
    return {
        "service": "devops-lab",
        "status": "ok",
        "version": "v3",
        "environment": APP_ENV

    }

@app.get("/health")
def health():
    return {"status": "healthy"}
