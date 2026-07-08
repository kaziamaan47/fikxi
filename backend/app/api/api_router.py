from fastapi import APIRouter

from app.api.category_routes import router as category_router
from app.api.health_routes import router as health_router


api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(category_router)