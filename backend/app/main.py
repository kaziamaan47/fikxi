from fastapi import FastAPI

from app.api.api_router import api_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for Fikxi, a multilingual local services marketplace.",
    version=settings.app_version,
)


app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "status": "running",
        "version": settings.app_version,
        "environment": settings.app_env,
    }