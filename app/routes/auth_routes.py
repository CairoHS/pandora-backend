from fastapi import APIRouter, HTTPException
from services.auth_service import AuthService
from services.token_service import TokenService
from fastapi.responses import JSONResponse
from schemas.usuario_schema import *



#bycript para hash de senha


router = APIRouter()

#observação resolver redundancia nos Schemas
@router.post("/cadastro", status_code=200)
async def cadastrar(dados_cadastro: InputCadastro):
    return AuthService.cadastrar(dados_cadastro)

@router.post("/login", status_code=200)
async def login(dados_login: InputLogin):
    return AuthService.login(dados_login)

@router.post("/refresh", status_code=200)
async def atualiza_token(token: InputRefresh):
    dados = TokenService.pega_dados_token(token.token)

    if not dados:
        HTTPException( status_code=401, detail="token invalido" )

    novo_token = TokenService.criar_acess_token(dados['sub'])

    return JSONResponse({"acess_token": "novo_token"}, status_code=200)

    
