from datetime import datetime
from pydantic import BaseModel

class DoctorMedicalSpecialtiesBase(BaseModel):
    doctor_id: int
    medical_specialty_id: int
    
class DoctorMedicalSpecialtiesCreate(DoctorMedicalSpecialtiesBase):
    pass

class DoctorMedicalSpecialtiesUpdate(DoctorMedicalSpecialtiesBase):
    pass

class DoctorMedicalSpecialties(DoctorMedicalSpecialtiesBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True