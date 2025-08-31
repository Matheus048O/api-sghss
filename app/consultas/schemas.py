# app/schemas/consulta_schema.py
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

class ConsultaBase(BaseModel):
    data_consulta: datetime
    id_paciente: Optional[int] 
    id_medico: int
    status: str  # <--- Adiciona isso aqui

    @field_validator('status')
    @classmethod
    def validar_status(cls, value):
        if value not in ['Confirmada', 'Cancelada', 'Realizada']:
            raise ValueError("Status inválido. Use: Confirmada, Cancelada ou Realizada.")
        return value

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaOut(ConsultaBase):
    id_consulta: int

    class Config:
        orm_mode = True
