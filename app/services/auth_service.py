from repository.usuario_repository import UsuarioRepository
from schemas.usuario_schema import *

from repository.usuario_repository import UsuarioRepository

from .criptografia_senha_service import CriptografiaSenhaService
from .token_service import TokenService

from fastapi import HTTPException
from fastapi.responses import JSONResponse

class AuthService():
    @staticmethod
    def cadastrar(dados_cadastro: InputCadastro) -> str:
        # Validar campos de entrada
        if len(dados_cadastro.nome) < 3 :
            raise "nome muito pequeno"
        
        if len(dados_cadastro.sobrenome) < 3:
            raise "sobrenome muito pequeno"
        
        if len(dados_cadastro.login) < 3:
            raise ""
        
        if not "@" in dados_cadastro.email:
            raise "email invalido"

        if len(dados_cadastro.email) < 3 :
            raise "email invalido" 
        
        if len(dados_cadastro.senha) < 8 :
            raise "senha muito pequena"
        
        if dados_cadastro.senha != dados_cadastro.comfirma_senha :
            raise "senha não batem"
        

        
        usuario_input = UsuarioComCredencial(
            nome= dados_cadastro.nome,
            sobrenome= dados_cadastro.sobrenome,
            email= dados_cadastro.email,
            login= dados_cadastro.login,
            senha= dados_cadastro.senha
            )

        # Ve se o email existe no banco
        
        if UsuarioRepository.usuario_existe(usuario_input.pega_usuario()):
           raise HTTPException(
               status_code= 409,
               detail="Usuario ou Email já existe"
           )


        # Criptografar Senha
        senha_criptograda = CriptografiaSenhaService.hash_senha(dados_cadastro.senha)

        usuario_input.senha = senha_criptograda
        

        UsuarioRepository.salvar_com_credencial(usuario_input)

        usuario_banco = UsuarioRepository.pegar_usuario(usuario_input.pega_usuario())


        token_acesso = TokenService.criar_acess_token(usuario_banco.id)
        token_refresh = TokenService.criar_refresh_token(usuario_banco.id)

        return JSONResponse({"acess_token": token_acesso,
                "refresh_token": token_refresh}, status_code=200)

    @staticmethod
    def login(dados_login: InputLogin) -> str:
        
        print(dados_login.model_dump)
        usuario_encontrado = UsuarioRepository.pegar_usuario(dados_login)
        
        if usuario_encontrado == None :
            raise HTTPException(
                status_code=403,
                detail="Usuario não existe"
            )
        
        if not CriptografiaSenhaService.verificar_senha(dados_login.senha, usuario_encontrado.senha) :
            raise HTTPException(
                status_code=401,
                detail="Senha incorreta"
            )
        
        token_acesso = TokenService.criar_acess_token(usuario_encontrado.id)
        token_refresh = TokenService.criar_refresh_token(usuario_encontrado.id)

        return JSONResponse({"acess_token": token_acesso,
                "refresh_token": token_refresh}, status_code=200)
        