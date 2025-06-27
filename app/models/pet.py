from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String)
    idade = Column(Integer)
    adotado = Column(Boolean, default=False)
