from sqlmodel import SQLModel, create_engine
from cache import pega_settings

#from models.credencial import Credencial
from models.usuario_model import UsuarioModel

url_banco: str = f"{pega_settings().ENDERECO_BANCO}?charset=utf8"

engine = create_engine(url_banco)

def cria_banco():
    try:
        SQLModel.metadata.create_all(engine)

    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    
