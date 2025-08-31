from sqlalchemy import Column, Integer, String
import enum
from app.database import Base
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.usuario_schema import TipoUsuario
from sqlalchemy.orm import relationship



class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    tipo = Column(String(20), nullable=False)

    consultas = relationship("Consulta", back_populates="medico")  # Relacionamento correto
