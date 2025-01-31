from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.models.doctors_model import Doctors
from src.schemas import doctor_schemas as schema

class DoctorService:
    def __init__(self, db: Session):
        self.db = db
        self.query = self.db.query(Doctors)
    
    def create(self, doctor: schema.DoctorCreate):
        doctor_has_register = self.query.filter(
            or_(
                Doctors.email==doctor.email,
                Doctors.crm==doctor.crm,
            )).first()
        
        if doctor_has_register:
            raise Exception("Doctor already exists with this email or crm")
        
        db_doctor = Doctors(**doctor.model_dump())
        self.db.add(db_doctor)
        self.db.commit()
        self.db.refresh(db_doctor)
        return db_doctor
    
    def get(self, skip: int = 0, limit: int = 100):
        return self.query.filter_by(status=True).offset(skip).limit(limit).all()
    
    def get_id(self, doctor_id: int):
        result = self.query.filter(
            Doctors.id ==doctor_id, 
            Doctors.status == True
            ).first()
        
        if result is None:
            raise Exception("Doctor not found")
        
        return result
    
    def update(self, id: int, doctor: schema.DoctorUpdate):
        db_doctor = self.query.filter_by(id=id).first()
        if not db_doctor:
            raise Exception("Doctor not found")
        
        db_doctor.name = doctor.name
        db_doctor.crm = doctor.crm
        db_doctor.phone = doctor.phone
        db_doctor.email = doctor.email
        self.db.commit()
        self.db.refresh(db_doctor)
        return db_doctor
    
    def delete(self, doctor_id: int):
        db_doctor = self.query.filter_by(id=doctor_id).first()
        
        if not db_doctor:
            raise Exception("Doctor not found")
        
        db_doctor.status = False
        self.db.commit()
        self.db.refresh(db_doctor)
        return db_doctor