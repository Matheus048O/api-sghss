# app/routers/consulta_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.consultas.schemas import ConsultaCreate, ConsultaOut
from app.consultas.crud import create_consulta, get_consulta_by_id, get_consultas, delete_consulta
from app.core.database import get_database_session
from app.auth.jwt_handler import get_usuario_atual

consulta_api_router = APIRouter()

@consulta_api_router.post("/", response_model=ConsultaOut)
def criar_consulta(
    consulta: ConsultaCreate,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)  # ✅ Protegido com token
):
    id_usuario = usuario_logado.get("id")
    return create_consulta(db=db, consulta=consulta, id_usuario_atuante=id_usuario)


@consulta_api_router.get("/", response_model=list[ConsultaOut])
def listar_consultas(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)  # ✅ Agora protegido
):
    return get_consultas(db=db, skip=skip, limit=limit)


@consulta_api_router.get("/{consulta_id}", response_model=ConsultaOut)
def obter_consulta(
    consulta_id: int,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)  # ✅ Agora protegido
):
    consulta = get_consulta_by_id(db, consulta_id)
    if consulta is None:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return consulta


@consulta_api_router.delete("/{consulta_id}", response_model=ConsultaOut)
def excluir_consulta(
    consulta_id: int,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)  # ✅ Protegido com token
):
    id_usuario = usuario_logado.get("id")
    return delete_consulta(db=db, consulta_id=consulta_id, id_usuario_atuante=id_usuario)
