# app/models.py

# app/models.py
from sqlalchemy import Column, Integer, String, Boolean, Text, Float
from sqlalchemy.dialects.postgresql import JSONB # Importamos el tipo JSONB
from database import Base

# app/models.py


class Movie(Base):
    """
    Modelo SQLAlchemy para películas.
    """
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    categoria = Column(String(50))
    ano = Column(Integer)
    director = Column(String(100))
    duracion = Column(Integer)  # en minutos
    calificacion = Column(Float)  # 0.0 a 10.0