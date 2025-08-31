from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Prontuario(Base):
    __tablename__ = "prontuarios"

    id_prontuario = Column(Integer, primary_key=True, index=True)
    id_consulta = Column(Integer, ForeignKey("consultas.id_consulta", ondelete="CASCADE"))

    descricao = Column(Text)
    receita = Column(Text)
    observacoes = Column(Text)

    consulta = relationship("Consulta", back_populates="prontuario")
