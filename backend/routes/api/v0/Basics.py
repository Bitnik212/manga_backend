from fastapi import APIRouter, Depends, HTTPException
from app.Http.Helpers import ResponseBuilder

router = APIRouter()

@router.get("/health")
async def health():
    return ResponseBuilder().success()


