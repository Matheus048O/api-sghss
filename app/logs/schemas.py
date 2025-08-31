from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogBase(BaseModel):
    id_usuario: Optional[int]
    acao: str
    tabela_afetada: str
    registro_id: Optional[int]
    observacoes: Optional[str]

class LogCreate(LogBase):
    pass

class LogOut(LogBase):
    id_log: int
    data_hora: datetime

    class Config:
        orm_mode = True
