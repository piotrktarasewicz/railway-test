import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "env_keys": list(os.environ.keys())
    }
