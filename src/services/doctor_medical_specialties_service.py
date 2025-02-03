from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.models.doctor_medical_specialties_model import DoctorMedicalSpecialties
from src.schemas import doctor_mecidal_specialties_schemas as schema

class DoctorMedicalSpecialtyService:
    def __init__(self, db: Session):
        self.db = db
        self.query = self.db.query(DoctorMedicalSpecialties)
    
    def create(self, doctor_medical_specialties: schema.DoctorMedicalSpecialtiesCreate):
        doctor_has_register_with_specialty = self.query.filter(
            or_(
                DoctorMedicalSpecialties.doctor_id==doctor_medical_specialties.doctor_id,
                DoctorMedicalSpecialties.medical_specialty_id==doctor_medical_specialties.medical_specialty_id,
            )).first()
        
        if doctor_has_register_with_specialty:
            raise Exception("Doctor already exists with this specialty")
        
        db_doctor_medical_specialty = DoctorMedicalSpecialties(**doctor_medical_specialties.model_dump())
        self.db.add(db_doctor_medical_specialty)
        self.db.commit()
        self.db.refresh(db_doctor_medical_specialty)
        return db_doctor_medical_specialty
    
    def get(self, skip: int = 1, limit: int = 100):
        return self.query.filter_by(status=True).offset(skip-1).limit(limit).all()
    
    def get_id(self, doctor_medical_specialty_id: int):
        result = self.query.filter(
            DoctorMedicalSpecialties.id ==doctor_medical_specialty_id, 
            DoctorMedicalSpecialties.status == True
            ).first()
        
        if result is None:
            raise Exception("Doctor medidal specialty not found")
        
        return result
    
    def update(self, id: int, doctor_medical_specialty: schema.DoctorMedicalSpecialtiesUpdate):
        db_doctor_medical_specialty = self.query.filter_by(id=id).first()
        if not db_doctor_medical_specialty:
            raise Exception("Doctor medidal specialty not found")
        
        db_doctor_medical_specialty.name = db_doctor_medical_specialty.name
        db_doctor_medical_specialty.crm = db_doctor_medical_specialty.crm
        db_doctor_medical_specialty.phone = db_doctor_medical_specialty.phone
        db_doctor_medical_specialty.email = db_doctor_medical_specialty.email
        
        self.db.commit()
        self.db.refresh(db_doctor_medical_specialty)
        return db_doctor_medical_specialty
    
    def delete(self, doctor_medical_specialty_id: int):
        db_doctor_medical_specialty = self.query.filter_by(id=doctor_medical_specialty_id).first()
        
        if not db_doctor_medical_specialty:
            raise Exception("Doctor medical specialty not found")
        
        db_doctor_medical_specialty.status = False
        self.db.commit()
        self.db.refresh(db_doctor_medical_specialty)
        return db_doctor_medical_specialty