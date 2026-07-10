from fastapi import FastAPI

app = FastAPI(title="CodeForge API")

@app.get("/")
def read_root():
    return {"status": "CodeForge backend is alive"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
