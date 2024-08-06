from pydantic import BaseModel
from dataclasses import dataclass, field

from .credencial_schema import Credencial





@dataclass
class Usuario():
    login: str
    senha: str
    email: str = field(default=None)
    id : int = field(default=None)

class InputCadastro(BaseModel):
    nome: str
    sobrenome: str
    email: str
    login: str
    senha: str
    comfirma_senha: str

class InputLogin(BaseModel):
    login: str
    senha: str

@dataclass
class UsuarioComCredencial():
    nome: str
    sobrenome: str
    email: str
    login: str
    senha: str

    def pega_usuario(self) -> Usuario:
        return Usuario(login = self.login,
                       senha = self.senha,
                       email = self.email)
    
    def pega_credencial(self) -> Credencial:
        return Credencial(self.nome, self.sobrenome)