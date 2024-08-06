from models.usuario_model import UsuarioModel
from db.dependencias import pega_session
from sqlmodel import select, or_
from models.usuario_model import UsuarioModel

from schemas.usuario_schema import *
from typing import Optional, Any

class UsuarioRepository:

    @staticmethod
    def salvar(novo_usuario: Usuario):
        with pega_session() as session:
            try:
                usuario = UsuarioModel(
                    login = novo_usuario.login,
                    email = novo_usuario.email,
                    senha = novo_usuario.senha,
                    tipo = 0,
                    estado = 0
                    )
                session.add(usuario)
                session.commit()

            except Exception as e:
                session.rollback()
                raise e

    @staticmethod
    def salvar_com_credencial(dados: UsuarioComCredencial) -> Any:
        UsuarioRepository.salvar(dados.pega_usuario())
    
    @staticmethod
    def pegar_usuario(usuario: Usuario) -> Optional[Usuario]:
        with pega_session() as session:
            try:
                query = select(UsuarioModel).where(UsuarioModel.login == usuario.login)
                resultado = session.exec(query).first()

                if (resultado == None):
                    return None

                return resultado

            except Exception as e:
                session.rollback()
                raise e
        
    @staticmethod
    def usuario_existe(usuario: Usuario) -> bool:
        with pega_session() as session:
            try:
                query = select(UsuarioModel).where(
                    or_(
                    UsuarioModel.login == usuario.login ,
                    UsuarioModel.email == usuario.email
                    )
                )
                resultado = session.exec(query).first()

                if (resultado == None):
                    return False

                return True

            except Exception as e:
                raise e

    @staticmethod
    def pega_usuario_pelo_id(id_usuario: str) -> Optional[Usuario]:
        with pega_session() as session:
            try:
                query = select(UsuarioModel).where(UsuarioModel.id == id_usuario)
                resultado = session.exec(query).first()

                if resultado == None:
                    return None

                return resultado

            except Exception as e:
                session.rollback()
                raise e

