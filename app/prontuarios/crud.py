from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.prontuarios.models import Prontuario
from app.prontuarios.schemas import ProntuarioCreate
from app.shared.crud import registrar_evento_log

def create_prontuario(db: Session, prontuario: ProntuarioCreate):
    db_prontuario = Prontuario(**prontuario.dict())
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)

    # LOG: criação de prontuário
    registrar_evento_log(db, None, "CREATE", "prontuarios", db_prontuario.id_prontuario, f"Prontuário criado para consulta ID {db_prontuario.id_consulta}")

    return db_prontuario

def get_prontuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Prontuario).offset(skip).limit(limit).all()

def get_prontuario_by_id(db: Session, prontuario_id: int):
    return db.query(Prontuario).filter(Prontuario.id_prontuario == prontuario_id).first()

def delete_prontuario(db: Session, prontuario_id: int):
    prontuario = get_prontuario_by_id(db, prontuario_id)
    if prontuario is None:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")

    db.delete(prontuario)
    db.commit()

    # LOG: exclusão de prontuário
    registrar_evento_log(db, None, "DELETE", "prontuarios", prontuario_id, f"Prontuário excluído (consulta ID {prontuario.id_consulta})")

    return prontuario
