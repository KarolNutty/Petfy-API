from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.crud import pet as crud_pet
from app.schemas import pet as schemas_pet

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pets", response_model=list[schemas_pet.PetOut])
def read_pets(db: Session = Depends(get_db)):
    return crud_pet.get_pets(db)

@router.get("/pets/{pet_id}", response_model=schemas_pet.PetOut)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = crud_pet.get_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return pet

@router.post("/pets", response_model=schemas_pet.PetOut)
def create_pet(pet: schemas_pet.PetCreate, db: Session = Depends(get_db)):
    return crud_pet.create_pet(db, pet)

@router.put("/pets/{pet_id}", response_model=schemas_pet.PetOut)
def update_pet(pet_id: int, pet: schemas_pet.PetUpdate, db: Session = Depends(get_db)):
    return crud_pet.update_pet(db, pet_id, pet)

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    return crud_pet.delete_pet(db, pet_id)
