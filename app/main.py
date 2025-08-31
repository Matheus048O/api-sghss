from fastapi import FastAPI
from app.usuarios import routers as usuario_api_router
from app.pacientes import routers as paciente_api_router
from app.consultas import routers as consulta_api_router
from app.prontuarios import routers as prontuario_api_router
from app.logs import routers as logs_api_router

api_principal = FastAPI()


# Incluindo o router com o prefixo correto
api_principal.include_router(usuario_api_router.usuario_api_router, prefix="/usuarios", tags=["usuarios"])
api_principal.include_router(paciente_api_router.paciente_api_router, prefix="/pacientes")
api_principal.include_router(consulta_api_router.consulta_api_router, prefix="/consultas", tags=["consultas"])
api_principal.include_router(prontuario_api_router.prontuario_api_router, prefix="/prontuarios", tags=["Prontuários"])
api_principal.include_router(logs_api_router.logs_api_router, prefix="/logs", tags=["Logs"])

@api_principal.get("/")
def read_root():
    return {"message": "Welcome to SGHSS API!"}
