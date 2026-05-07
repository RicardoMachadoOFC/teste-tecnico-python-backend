
# perguntado ao gpt se existia algum import que ajudasse em validações e verificações, encontrei o pydantic.
# BaseModel para criar modelos de dados e Field para adicionar as validações
from pydantic import BaseModel, Field


class RegistroCreate(BaseModel):
    #Field fazendo com que o campo seja obrigatório e >= 1 <=5
    nivel_foco: int = Field(..., ge=1, le=5)

    #seguindo a mesma lógica os outros campos são obrigatórios de acordo com o tipo.
    tempo_minutos: int
    comentario: str
    categoria: str