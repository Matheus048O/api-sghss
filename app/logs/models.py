from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class Log(Base):
    __tablename__ = "logs"

    id_log = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"), nullable=True)
    acao = Column(String, nullable=False)
    tabela_afetada = Column(String, nullable=False)
    registro_id = Column(Integer, nullable=False)
    data_hora = Column(DateTime(timezone=True), server_default=func.now())
    observacoes = Column(Text)
