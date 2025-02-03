from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import doctor_medical_specialties_model as model
from src.schemas import doctor_mecidal_specialties_schemas as schemas
from src.services import doctor_medical_specialties_service as service
from src.infra import database

router = APIRouter(prefix='/doctors-medical-specialties', tags=["Doctors-Medical-Specialties"])

def get_doctor_medical_specialty_service(db: Session = Depends(database.get_db)):
    return service.DoctorMedicalSpecialtyService(db=db)

@router.post("/", response_model=schemas.DoctorMedicalSpecialtiesCreate, summary="Create a new doctor medical specialty")
def post(doctor_medical_specialty: schemas.DoctorMedicalSpecialtiesCreate, service: service.DoctorMedicalSpecialtyService = Depends(get_doctor_medical_specialty_service)):
    try:
        return service.create(doctor_medical_specialties=doctor_medical_specialty)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[schemas.DoctorMedicalSpecialties], summary="Get all doctors medical specialties")
def get(skip: int = 1, limit: int = 10, service: service.DoctorMedicalSpecialties = Depends(get_doctor_medical_specialty_service)):
    try:
        return service.get(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{doctor_medical_specialty_id}", response_model=schemas.DoctorMedicalSpecialties, summary="Get a doctor medical specialty by id")
def get_id(doctor_medical_specialty_id: int, service: service.DoctorMedicalSpecialties = Depends(get_doctor_medical_specialty_service)):
    try:
        return service.get_id(doctor_medical_specialty_id=doctor_medical_specialty_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{doctor_medical_specialty_id}", response_model=schemas.DoctorMedicalSpecialties, summary="Update a doctor medical specialty by id")
def put(doctor_medical_specialty_id: int, doctor_medical_specialty: schemas.DoctorMedicalSpecialtiesUpdate, service: service.DoctorMedicalSpecialties = Depends(get_doctor_medical_specialty_service)):
    try:
        return service.update(id=doctor_medical_specialty_id, doctor=doctor_medical_specialty)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{doctor_medical_specialty_id}", response_model=schemas.DoctorMedicalSpecialties, summary="Delete a doctor by id")
def delete(doctor_medical_specialty_id: int, service: service.DoctorMedicalSpecialties = Depends(get_doctor_medical_specialty_service)):
    try:
        return service.delete(doctor_medical_specialty_id=doctor_medical_specialty_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))