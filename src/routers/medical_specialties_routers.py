from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import medical_specialties_model as model
from src.schemas import medical_specialties_schemas as schemas
from src.services import medical_specialties_services as service
from src.infra import database

router = APIRouter(prefix='/medical-specialties', tags=["Medical Specialties"])
def get_medical_specialty_service(db: Session = Depends(database.get_db)):
    return service.MedicalSpecialtyService(db=db)

@router.post("/", response_model=schemas.MedicalSpecialties, summary="Create a new medical specialty")
def post(medical_specialty: schemas.MedicalSpecialtiesCreate, service: service.MedicalSpecialtyService = Depends(get_medical_specialty_service)):
    try:
        return service.create(medical_specialty=medical_specialty)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=List[schemas.MedicalSpecialties], summary="Get all medical specialties")
def get(skip: int = 1, limit: int = 10, service: service.MedicalSpecialtyService = Depends(get_medical_specialty_service)):
    try:
        return service.get(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties, summary="Get a medical specialty by id")
def get_id(medical_specialty_id: int, service: service.MedicalSpecialtyService = Depends(get_medical_specialty_service)):
    try:
        return service.get_id(medical_specialty_id=medical_specialty_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties, summary="Update a medical specialty by id")
def put(medical_specialty_id: int, medical_specialty: schemas.MedicalSpecialtiesUpdate, service: service.MedicalSpecialtyService = Depends(get_medical_specialty_service)):
    try:
        return service.update(id=medical_specialty_id, medical_specialty=medical_specialty)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{medical_specialty_id}", response_model=schemas.MedicalSpecialties, summary="Delete a medical specialty by id")
def delete(medical_specialty_id: int, service: service.MedicalSpecialtyService = Depends(get_medical_specialty_service)):
    try:
        return service.delete(medical_specialty_id=medical_specialty_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))