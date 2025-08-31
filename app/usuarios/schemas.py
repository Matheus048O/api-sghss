from pydantic import BaseModel
from enum import Enum

# Enums para os tipos de usuário
class TipoUsuario(str, Enum):
    admin = "admin"
    medico = "medico"
    recepcionista = "recepcionista"

# Schema para criação de usuários
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    tipo: TipoUsuario  # Alterado de 'papel' para 'tipo'

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Schema de saída de usuários
class UsuarioOut(BaseModel):
    id_usuario: int
    nome: str
    email: str
    tipo: TipoUsuario  # Alterado de 'papel' para 'tipo'

#shema para autenticae
class LoginRequest(BaseModel):
    email: str
    senha: str


class Config:
    orm_mode = True


