from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import medical_specialties_model as model
from src.schemas import medical_specialties_schemas as schemas
from src.services import medical_specialties_services as service
from src.infra import database

router = APIRouter(prefix='/medical-specialties', tags=["Medical Specialties"])

@router.post("/", response_model=schemas.MedicalSpecialties)
def create_medical_specialty(medical_specialty: schemas.MedicalSpecialtiesCreate, db: Session = Depends(database.get_db)):
    try:
        return service.create_medical_specialty(medical_specialty=medical_specialty, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=List[schemas.MedicalSpecialties])
def get_medial_specialties(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    try:
        return service.get_medical_specialties(db=db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties)
def get_medical_specialty(medical_specialty_id: int, db: Session = Depends(database.get_db)):
    try:
        return service.get_medical_specialty(db=db, medical_specialty_id=medical_specialty_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties)
def update_medical_specialty(medical_specialty_id: int, medical_specialty: schemas.MedicalSpecialtiesUpdate, db: Session = Depends(database.get_db)):
    try:
        return service.update_medical_specialty(id=medical_specialty_id, medical_specialty=medical_specialty, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties)
def deactivate_medical_specialty(medical_specialty_id: int, db: Session = Depends(database.get_db)):
    try:
        return service.deactivate_medical_specialty(medical_specialty_id=medical_specialty_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))