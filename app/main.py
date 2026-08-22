from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "service": "devops-lab",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
