from fastapi import APIRouter
from src.user.router import router as users_router
from src.breed.router import router as breeds_router
from src.kitty.router import router as kittens_router

api_router = APIRouter()

api_router.include_router(users_router, tags=["user"])
api_router.include_router(breeds_router, tags=["breed"])
api_router.include_router(kittens_router, tags=["kitty"])
