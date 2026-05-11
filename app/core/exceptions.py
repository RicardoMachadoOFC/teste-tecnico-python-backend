from fastapi import HTTPException


class NivelFocoInvalidoException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="nivel_foco deve estar entre 1 e 5"
        )


class TempoInvalidoException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="tempo_minutos deve ser maior que 0"
        )