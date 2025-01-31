from sqlalchemy.orm import Session
from src.models import doctors_model as model
from src.schemas import doctor_schemas as schema

class DoctorService:
    def __init__(self, db: Session):
        self.db = db
        self.model = model.Doctors
        self.query = self.db.query(self.model)
    
    def create(self, doctor: schema.DoctorCreate):
        db_doctor = self.model(**doctor.model_dump())
        self.db.add(db_doctor)
        self.db.commit()
        self.db.refresh(db_doctor)
        return db_doctor
    
    def get(self, skip: int = 0, limit: int = 100):
        return self.query.filter_by(status=True).offset(skip).limit(limit).all()
    
    def get_id(self, doctor_id: int):
        result = self.query.filter(
            self.model.id ==doctor_id, 
            self.model.status == True
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