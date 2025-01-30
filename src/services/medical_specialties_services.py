from sqlalchemy.orm import Session
from src.models import medical_specialties_model as model
from src.schemas import medical_specialties_schemas as schema

def create_medical_specialty(medical_specialty: schema.MedicalSpecialtiesCreate, db: Session):
    db_medical_specialty_has_register = db.query(model.MedicalSpecialties).filter_by(name=medical_specialty.name).first()
    
    if db_medical_specialty_has_register:
        raise Exception("Medical Specialty already exists")
    
    db_medical_specialty = model.MedicalSpecialties(**medical_specialty.model_dump())
    db.add(db_medical_specialty)
    db.commit()
    db.refresh(db_medical_specialty)
    return db_medical_specialty

def get_medical_specialties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.MedicalSpecialties).filter_by(status=True).offset(skip).limit(limit).all()

def get_medical_specialty(db: Session, medical_specialty_id: int):
    result = db.query(model.MedicalSpecialties).filter(
        model.MedicalSpecialties.id ==medical_specialty_id, 
        model.MedicalSpecialties.status == True
        ).first()
    
    if result is None:
        raise Exception("Medical Specialty not found")
    
    return result

def update_medical_specialty(id: int, medical_specialty: schema.MedicalSpecialtiesUpdate, db: Session):
    db_medical_specialty = db.query(model.MedicalSpecialties).filter_by(id=id).first()
    if not db_medical_specialty:
        raise Exception("Medical Specialty not found")
    
    db_medical_specialty.name = medical_specialty.name
    db_medical_specialty.description = medical_specialty.description
    db.commit()
    db.refresh(db_medical_specialty)
    return db_medical_specialty

def deactivate_medical_specialty(medical_specialty_id: int, db: Session):
    db_medical_specialty = db.query(model.MedicalSpecialties).filter_by(id=medical_specialty_id).first()
    
    if not db_medical_specialty:
        raise Exception("Medical Specialty not found")
    
    db_medical_specialty.status = False
    db.commit()
    db.refresh(db_medical_specialty)
    return db_medical_specialty