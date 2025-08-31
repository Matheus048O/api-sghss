from pydantic import BaseModel
from typing import Optional
class ProntuarioBase(BaseModel):
    id_consulta: Optional[int]
    descricao: str
    receita: str
    observacoes: str

class ProntuarioCreate(ProntuarioBase):
    pass

class ProntuarioOut(ProntuarioBase):
    id_prontuario: int

    class Config:
        orm_mode = True
