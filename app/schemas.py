from pydantic import BaseModel, Field
from datetime import datetime


class RegistroCreate(BaseModel):

    nivel_foco: int = Field(
        ...,
        ge=1,
        le=5,
        description="Nível de foco de 1 até 5"
    )

    tempo_minutos: int = Field(
        ...,
        gt=0,
        description="Tempo da sessão em minutos"
    )

    comentario: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Comentário da sessão"
    )

    categoria: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Categoria da atividade"
    )

    data_criacao: datetime = datetime.now()