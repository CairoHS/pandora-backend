from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class Credencial():
    nome: str
    sobrenome: str
    