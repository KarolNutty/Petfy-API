from sqlalchemy.orm import Session
from app.models.pet import Pet
from app.schemas.pet import PetCreate, PetUpdate

def get_pets(db: Session):
    return db.query(Pet).all()

def get_pet(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()

def create_pet(db: Session, pet: PetCreate):
    db_pet = Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet(db: Session, pet_id: int, pet_data: PetUpdate):
    db_pet = get_pet(db, pet_id)
    if db_pet:
        for key, value in pet_data.dict().items():
            setattr(db_pet, key, value)
        db.commit()
        db.refresh(db_pet)
    return db_pet

def delete_pet(db: Session, pet_id: int):
    db_pet = get_pet(db, pet_id)
    if db_pet:
        db.delete(db_pet)
        db.commit()
    return db_pet
