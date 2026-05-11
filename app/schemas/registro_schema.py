from pydantic import BaseModel, Field


class RegistroCreate(BaseModel):

    nivel_foco: int = Field(..., ge=1, le=5)

    tempo_minutos: int

    comentario: str

    categoria: str