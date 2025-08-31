from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.jwt_handler import verificar_senha, criar_token_acesso, get_usuario_atual
from app.usuarios.schemas import UsuarioCreate, UsuarioOut, Token, LoginRequest
from app.core.database import get_database_session
from app.shared import crud

usuario_api_router = APIRouter()

@usuario_api_router.post("/", response_model=UsuarioOut)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)  # ⬅️ Pega o usuário autenticado
):
    db_usuario = crud.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    return crud.create_usuario(
        db=db,
        usuario=usuario,
        id_usuario_atuante=usuario_logado.get("id")  # ⬅️ Pega o ID do token
    )

@usuario_api_router.get("/", response_model=list[UsuarioOut])
def get_usuarios(db: Session = Depends(get_database_session)):
    return crud.get_usuarios(db=db)

@usuario_api_router.get("/{usuario_id}", response_model=UsuarioOut)
def get_usuario(usuario_id: int, db: Session = Depends(get_database_session)):
    db_usuario = crud.get_usuario_by_id(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@usuario_api_router.post("/login", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_database_session)):
    usuario = crud.get_usuario_by_email(db, login_data.email)
    if not usuario or not verificar_senha(login_data.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Inclui o id_usuario no token para logs
    token = criar_token_acesso({
        "sub": usuario.email,
        "tipo": usuario.tipo,
        "id": usuario.id_usuario  # ⬅️ necessário para os logs
    })
    return {"access_token": token, "token_type": "bearer"}
@usuario_api_router.put("/{usuario_id}", response_model=UsuarioOut)
def atualizar_usuario(
    usuario_id: int,
    usuario_atualizado: UsuarioCreate,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)
):
    return crud.update_usuario(
        db=db,
        usuario_id=usuario_id,
        usuario_atualizado=usuario_atualizado,
        id_usuario_atuante=usuario_logado.get("id")
    )

@usuario_api_router.delete("/{usuario_id}", response_model=UsuarioOut)
def deletar_usuario(
    usuario_id: int,
    db: Session = Depends(get_database_session),
    usuario_logado: dict = Depends(get_usuario_atual)
):
    return crud.delete_usuario(
        db=db,
        usuario_id=usuario_id,
        id_usuario_atuante=usuario_logado.get("id")
    )

