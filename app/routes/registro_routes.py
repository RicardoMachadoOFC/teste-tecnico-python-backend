from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.schemas.registro_schema import RegistroCreate
from app.models.registro import Registro
from app.database import SessionLocal
from app.services.diagnostico_service import gerar_diagnostico
from app.core.exceptions import NivelFocoInvalidoException, TempoInvalidoException

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/registro-foco")
def criar_registro(registro: RegistroCreate, db: Session = Depends(get_db)):

    if registro.nivel_foco < 1 or registro.nivel_foco > 5:
        raise NivelFocoInvalidoException()

    if registro.tempo_minutos <= 0:
        raise TempoInvalidoException()

    novo = Registro(
        nivel_foco=registro.nivel_foco,
        tempo_minutos=registro.tempo_minutos,
        comentario=registro.comentario,
        categoria=registro.categoria
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return {"mensagem": "Registro salvo", "id": novo.id}


@router.get("/registros")
def listar_registros(data: date = None, db: Session = Depends(get_db)):

    query = db.query(Registro)

    if data:
        query = query.filter(Registro.data_criacao.like(f"{data}%"))

    return query.all()


@router.get("/diagnostico-produtividade")
def diagnostico(db: Session = Depends(get_db)):

    registros = db.query(Registro).all()

    return gerar_diagnostico(registros)