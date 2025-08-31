from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.prontuarios.schemas import ProntuarioCreate, ProntuarioOut
from app.prontuarios.crud import (
    create_prontuario,
    get_prontuarios,
    get_prontuario_by_id,
    delete_prontuario,
)
from app.core.database import get_database_session
prontuario_api_router = APIRouter()

@prontuario_api_router.post("/", response_model=ProntuarioOut)
def criar_prontuario(prontuario: ProntuarioCreate, db: Session = Depends(get_database_session)):
    return create_prontuario(db, prontuario)

@prontuario_api_router.get("/", response_model=list[ProntuarioOut])
def listar_prontuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_database_session)):
    return get_prontuarios(db, skip, limit)

@prontuario_api_router.get("/{prontuario_id}", response_model=ProntuarioOut)
def obter_prontuario(prontuario_id: int, db: Session = Depends(get_database_session)):
    prontuario = get_prontuario_by_id(db, prontuario_id)
    if prontuario is None:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return prontuario

@prontuario_api_router.delete("/{prontuario_id}", response_model=ProntuarioOut)
def excluir_prontuario(prontuario_id: int, db: Session = Depends(get_database_session)):
    return delete_prontuario(db, prontuario_id)
