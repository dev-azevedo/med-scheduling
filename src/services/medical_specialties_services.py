
from sqlalchemy.orm import Session
from src.models.medical_specialties_model import MedicalSpecialties
from src.schemas import medical_specialties_schemas as schema

class MedicalSpecialtyService:
    def __init__(self, db: Session):
        self.db = db
        self.query = self.db.query(MedicalSpecialties)
        
    def create(self, medical_specialty: schema.MedicalSpecialtiesCreate):
        db_medical_specialty_has_register = self.query.filter_by(name=medical_specialty.name).first()
        
        if db_medical_specialty_has_register:
            raise Exception("Medical Specialty already exists")
        
        db_medical_specialty = MedicalSpecialties(**medical_specialty.model_dump())
        self.db.add(db_medical_specialty)
        self.db.commit()
        self.db.refresh(db_medical_specialty)
        return db_medical_specialty
    
    def get(self, skip: int = 0, limit: int = 100):
        return self.query.filter_by(status=True).offset(skip).limit(limit).all()
    
    def get_id(self, medical_specialty_id: int):
        result = self.query.filter(
            MedicalSpecialties.id ==medical_specialty_id, 
            MedicalSpecialties.status == True
            ).first()
        
        if result is None:
            raise Exception("Medical Specialty not found")
        
        return result
    
    def update(self, id: int, medical_specialty: schema.MedicalSpecialtiesUpdate):
        db_medical_specialty = self.query.filter_by(id=id).first()
        if not db_medical_specialty:
            raise Exception("Medical Specialty not found")
        
        db_medical_specialty.name = medical_specialty.name
        db_medical_specialty.description = medical_specialty.description
        self.db.commit()
        self.db.refresh(db_medical_specialty)
        return db_medical_specialty
    
    def delete(self, medical_specialty_id: int):
        db_medical_specialty = self.query.filter_by(id=medical_specialty_id).first()
        
        if not db_medical_specialty:
            raise Exception("Medical Specialty not found")
        
        db_medical_specialty.status = False
        self.db.commit()
        self.db.refresh(db_medical_specialty)
        return db_medical_specialty