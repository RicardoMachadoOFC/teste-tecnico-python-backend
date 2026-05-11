from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Registro(Base):

    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)

    nivel_foco = Column(Integer, nullable=False)

    tempo_minutos = Column(Integer, nullable=False)

    comentario = Column(String(255), nullable=False)

    categoria = Column(String(50), nullable=False)

    data_criacao = Column(DateTime, default=datetime.utcnow)