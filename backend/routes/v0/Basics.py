from fastapi import APIRouter, Depends, HTTPException
from app.Http.Helpers import ResponceBuilder

router = APIRouter()

router.get("/health")
async def health():
    return ResponceBuilder().success()

