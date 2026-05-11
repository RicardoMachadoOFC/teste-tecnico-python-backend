from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import RegistroCreate
from app.models import Registro
from app.database import SessionLocal
from app.services import gerar_diagnostico


router = APIRouter()


# cria sessão do banco
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/")
def home():

    return {"mensagem": "API funcionando"}


@router.post("/registro-foco")
def criar_registro(
    registro: RegistroCreate,
    db: Session = Depends(get_db)
):

    novo_registro = Registro(

        nivel_foco=registro.nivel_foco,
        tempo_minutos=registro.tempo_minutos,
        comentario=registro.comentario,
        categoria=registro.categoria
    )

    db.add(novo_registro)

    db.commit()

    db.refresh(novo_registro)

    return {
        "mensagem": "Registro salvo com sucesso",
        "id": novo_registro.id
    }


@router.get("/registros")
def listar_registros(db: Session = Depends(get_db)):

    registros = db.query(Registro).all()

    return registros


@router.get("/diagnostico-produtividade")
def diagnostico(db: Session = Depends(get_db)):

    registros = db.query(Registro).all()

    return gerar_diagnostico(registros)