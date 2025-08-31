# app/models/consulta_model.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.database import Base



class Consulta(Base):
    __tablename__ = "consultas"
    
    id_consulta = Column(Integer, primary_key=True, index=True)
    data_consulta = Column(DateTime, nullable=False)
    id_paciente = Column(Integer, ForeignKey("pacientes.id_paciente"))
    id_medico = Column(Integer, ForeignKey("usuarios.id_usuario"))
    status = Column(String(20), nullable=False)  # <-- ESTA LINHA AQUI

    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Usuario", back_populates="consultas")
    prontuario = relationship("Prontuario", back_populates="consulta", uselist=False)

