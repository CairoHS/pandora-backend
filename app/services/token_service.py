
from datetime import datetime, timedelta, UTC
from cache import pega_settings

from repository.usuario_repository import UsuarioRepository

import jwt
#Aqui fica os token focados em login

class TokenService:
    #token de curto prazo para segurança

    @staticmethod
    def criar_acess_token(id_usuario: str):
        

        tempo = timedelta(minutes=pega_settings().MINUTOS_PARA_EXPIRAR_ACESS_TOKEN) + datetime.now(UTC)

        informacoes = {
            "id": id_usuario,
            "exp": tempo,
            "tipo_usuario": "0",
            "type": "acess",
            "assinatura": pega_settings().ALGORITMO 
        }

        token_jwt = jwt.encode(informacoes, pega_settings().CHAVE_SECRETA, algorithm=pega_settings().ALGORITMO)

        return token_jwt
    
    #token de longo prazo para não deslogar
    @staticmethod
    def criar_refresh_token(id_usuario: str):
         
        tempo = timedelta(hours=pega_settings().HORAS_PARA_EXPIRAR_REFRESH_TOKEN) + datetime.now(UTC)

        informacoes = {
            "id": id_usuario,
            "exp": tempo,
            "type": "refresh",
            "assinatura": pega_settings().ALGORITMO 
        }

        token_jwt = jwt.encode(informacoes, pega_settings().CHAVE_SECRETA, algorithm=pega_settings().ALGORITMO)

        return token_jwt


    #token para quando recuperar algo
    @staticmethod
    def criar_recovery_token():
        pass

    #só recuperar token
    @staticmethod
    def verificar_token(token_codificado: str):
        informacoes = jwt.decode(token_codificado, pega_settings().CHAVE_SECRETA, algorithms=[pega_settings().ALGORITMO])

        return informacoes
