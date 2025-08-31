# app/schemas/paciente_schema.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class PacienteBase(BaseModel):
    nome: str
    data_nascimento: date
    sexo: str
    cpf: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class PacienteCreate(PacienteBase):
    pass

class PacienteOut(PacienteBase):
    id_paciente: int

    class Config:
        orm_mode = True
