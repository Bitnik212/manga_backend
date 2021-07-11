from fastapi import APIRouter
from fastapi.responses import RedirectResponse
"""
Авторизация пользователя
"""
router = APIRouter()


@router.get("/")
async def sign_in_root():
    return RedirectResponse("docs")


