from sqlalchemy import Column, ForeignKey, Integer, String, Table

from .base_model import BaseModel, Base

class DoctorMedicalSpecialties(Base, BaseModel):
    __tablename__ = "doctor_medical_specialties"
    
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    medical_specialty_id = Column(Integer, ForeignKey("medical_specialties.id"), nullable=False)
