from fastapi import APIRouter, Depends, Response
from services.auth_service import AuthService

from schemas.usuario_schema import *

#bycript para hash de senha


router = APIRouter()

#observação resolver redundancia nos Schemas
@router.post("/cadastro")
async def cadastrar(dados_cadastro: InputCadastro):
    return AuthService.cadastrar(dados_cadastro)

@router.post("/login", status_code=200)
async def login(dados_login: InputLogin):
    return AuthService.login(dados_login)