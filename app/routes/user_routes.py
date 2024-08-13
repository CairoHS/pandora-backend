from fastapi import APIRouter
from services.auth_service import AuthService

from schemas.usuario_schema import *

#bycript para hash de senha


router = APIRouter()

#observação resolver redundancia nos Schemas
@router.get("/")
def valida():
    return {"teste": "teste"}