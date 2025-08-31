from fastapi import FastAPI
from app.core.database import engine, Base

# --- IMPORTANTE ---
# Importa a variável do roteador de cada arquivo de rotas
from app.auth.routers import auth_api_router
from app.consultas.routers import consulta_api_router
from app.pacientes.routers import paciente_api_router
from app.prontuarios.routers import prontuario_api_router
from app.usuarios.routers import usuario_api_router

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API SGHSS")

# --- IMPORTANTE ---
# Inclui cada roteador na aplicação principal, definindo o prefixo da URL
app.include_router(auth_api_router, prefix="/auth", tags=["Autenticação"])
app.include_router(consulta_api_router, prefix="/consultas", tags=["Consultas"])
app.include_router(paciente_api_router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(prontuario_api_router, prefix="/prontuarios", tags=["Prontuários"])
app.include_router(usuario_api_router, prefix="/usuarios", tags=["Usuários"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do SGHSS"}