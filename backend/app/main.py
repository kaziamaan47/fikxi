from fastapi import FastAPI

app = FastAPI(
    title="Fikxi API",
    description="Backend API for Fikxi, a multilingual local services marketplace.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Fikxi API",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }