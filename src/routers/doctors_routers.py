from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models import doctors_model as model
from src.schemas import doctor_schemas as schemas
from src.services import doctor_services as service
from src.infra import database

router = APIRouter(prefix='/doctors', tags=["Doctors"])

def get_doctor_service(db: Session = Depends(database.get_db)):
    return service.DoctorService(db=db)

@router.post("/", response_model=schemas.Doctor)
def post(doctor: schemas.DoctorCreate, service: service.DoctorService = Depends(get_doctor_service)):
    try:
        return service.create(doctor=doctor)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[schemas.Doctor])
def get(skip: int = 1, limit: int = 10, service: service.DoctorService = Depends(get_doctor_service)):
    try:
        return service.get(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{doctor_id}", response_model=schemas.Doctor)
def get_id(doctor_id: int, service: service.DoctorService = Depends(get_doctor_service)):
    try:
        return service.get_id(doctor_id=doctor_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{doctor_id}", response_model=schemas.Doctor)
def put(doctor_id: int, doctor: schemas.DoctorUpdate, service: service.DoctorService = Depends(get_doctor_service)):
    try:
        return service.update(id=doctor_id, doctor=doctor)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{doctor_id}", response_model=schemas.Doctor)
def delete(doctor_id: int, service: service.DoctorService = Depends(get_doctor_service)):
    try:
        return service.delete(doctor_id=doctor_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))