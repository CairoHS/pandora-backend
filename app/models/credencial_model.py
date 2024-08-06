from typing import Optional
from sqlmodel import SQLModel, Field, Column, String, Relationship

class CredencialModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(sa_column=Column(String(45), nullable=False))
    sobrenome: str = Field(sa_column=Column(String(150), nullable=False))
    id_usuario: int | None = Field(default=None, foreign_key="usuariomodel.id")
    usuario: Optional['UsuarioModel'] = Relationship(back_populates="credencial")

