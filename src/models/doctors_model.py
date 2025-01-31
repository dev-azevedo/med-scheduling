from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel, Base
from .doctor_medical_specialties_model import DoctorMedicalSpecialties

class Doctors(Base, BaseModel):
    __tablename__ = "doctors"
    
    name = Column(String, nullable=False, index=True)
    crm = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    medical_specialties = relationship("MedicalSpecialties", secondary=DoctorMedicalSpecialties.__tablename__, back_populates="doctors")