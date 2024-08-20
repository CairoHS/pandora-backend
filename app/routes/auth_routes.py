from fastapi import APIRouter, HTTPException
from services.auth_service import AuthService
from services.token_service import TokenService
from fastapi.responses import JSONResponse
from schemas.usuario_schema import *
from repository.usuario_repository import UsuarioRepository

# bycript para hash de senha


router = APIRouter()

# observação resolver redundancia nos Schemas


@router.post("/validacao")
async def validacao(email_validacao: InputValidacao):
    usuario = UsuarioRepository.pegar_usuario_pelo_email(email_validacao.email)
    if usuario == None:
        return JSONResponse({"Error": "Email inválido"}, status_code=400)


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
        HTTPException(status_code=401, detail="token invalido")

    novo_token = TokenService.criar_acess_token(dados['sub'])

    return JSONResponse({"acess_token": "novo_token"}, status_code=200)
