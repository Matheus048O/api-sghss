from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id_paciente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(String(1), nullable=False)
    cpf = Column(String(11), nullable=False)
    telefone = Column(String(20), nullable=True)
    endereco = Column(Text, nullable=True)

    consultas = relationship("Consulta", back_populates="paciente")
