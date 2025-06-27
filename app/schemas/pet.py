from pydantic import BaseModel, ConfigDict

class PetBase(BaseModel):
    nome: str
    tipo: str
    idade: int
    adotado: bool = False

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass

class PetOut(PetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
