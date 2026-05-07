from fastapi import APIRouter

from app.schemas import RegistroCreate

from app.services import gerar_diagnostico

router = APIRouter()

registros = []
# get apenas para testar se a api está retornando
@router.get("/")
def home():
    return {"API funcionando"}

@router.post("/registro-foco")
def criar_registro(registro: RegistroCreate):

    registros.append(registro)

    return {
        "mensagem": "Registro salvo com sucesso",
        "dados": registro.dict()
    }

@router.get("/diagnostico-produtividade")

def diagnostico():
            # pega todas as infos do service e separa por registros
            return gerar_diagnostico(registros)