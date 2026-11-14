"""python-backend — FastAPI service."""
from fastapi import FastAPI

app = FastAPI(title="python-backend")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    return {"app": "python-backend", "project": "orchid"}
