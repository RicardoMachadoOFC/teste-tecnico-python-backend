from fastapi import APIRouter

from app.schemas import RegistroCreate
from app.services import gerar_diagnostico

router = APIRouter()

registros = []


# GET apenas para testar se a API está funcionando
@router.get("/")
def home():

    return {"mensagem": "API funcionando"}


# POST para criar um novo registro
@router.post("/registro-foco")
def criar_registro(registro: RegistroCreate):

    registros.append(registro)

    return {
        "mensagem": "Registro salvo com sucesso",
        "dados": registro.dict()
    }


# GET para listar todos os registros
@router.get("/registros")
def listar_registros():

    return {
        "quantidade": len(registros),
        "registros": registros
    }


# GET para buscar registros por categoria
@router.get("/registros/categoria/{categoria}")
def buscar_por_categoria(categoria: str):

    registros_filtrados = []

    for registro in registros:

        if registro.categoria.lower() == categoria.lower():
            registros_filtrados.append(registro)

    return {
        "categoria": categoria,
        "quantidade": len(registros_filtrados),
        "registros": registros_filtrados
    }


# GET para gerar diagnóstico
@router.get("/diagnostico-produtividade")
def diagnostico():

    return gerar_diagnostico(registros)