# app/scripts/atualizar_senhas.py
from app.auth.jwt_handler import criar_hash_senha
from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.database import SessionLocal  # Ou o arquivo onde você cria a sessão do DB

def atualizar_senhas(db: Session):
    usuarios = db.query(Usuario).all()
    for usuario in usuarios:
        usuario.senha = criar_hash_senha(usuario.senha)
    db.commit()
    print("Senhas atualizadas com sucesso.")

if __name__ == "__main__":
    db = SessionLocal()  # Aqui você pega a sessão do banco
    atualizar_senhas(db)
