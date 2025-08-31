# app/crud/paciente_crud.py
from sqlalchemy.orm import Session
from app.pacientes.models import Paciente
from app.pacientes.schemas import PacienteCreate
from app.shared.crud import registrar_evento_log

def create_paciente(db: Session, paciente: PacienteCreate, id_usuario_atuante: int = None):
    db_paciente = Paciente(
        nome=paciente.nome,
        data_nascimento=paciente.data_nascimento,
        sexo=paciente.sexo,
        cpf=paciente.cpf,
        telefone=paciente.telefone,
        endereco=paciente.endereco
    )
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)

    if id_usuario_atuante:
        registrar_evento_log(db, id_usuario_atuante, "CREATE", "pacientes", db_paciente.id_paciente, "Paciente criado")

    return db_paciente

def get_pacientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Paciente).offset(skip).limit(limit).all()

def get_paciente_by_id(db: Session, paciente_id: int):
    return db.query(Paciente).filter(Paciente.id_paciente == paciente_id).first()

def update_paciente(db: Session, paciente_id: int, paciente: PacienteCreate, id_usuario_atuante: int = None):
    db_paciente = db.query(Paciente).filter(Paciente.id_paciente == paciente_id).first()
    if db_paciente:
        db_paciente.nome = paciente.nome
        db_paciente.data_nascimento = paciente.data_nascimento
        db_paciente.sexo = paciente.sexo
        db_paciente.cpf = paciente.cpf
        db_paciente.telefone = paciente.telefone
        db_paciente.endereco = paciente.endereco
        db.commit()
        db.refresh(db_paciente)

        if id_usuario_atuante:
            registrar_evento_log(db, id_usuario_atuante, "UPDATE", "pacientes", db_paciente.id_paciente, "Paciente atualizado")
    return db_paciente

def delete_paciente(db: Session, paciente_id: int, id_usuario_atuante: int = None):
    db_paciente = db.query(Paciente).filter(Paciente.id_paciente == paciente_id).first()
    if db_paciente:
        db.delete(db_paciente)
        db.commit()

        if id_usuario_atuante:
            registrar_evento_log(db, id_usuario_atuante, "DELETE", "pacientes", paciente_id, "Paciente deletado")
    return db_paciente
