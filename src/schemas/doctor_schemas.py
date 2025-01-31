from datetime import datetime
from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    crm: str
    phone: str
    email: str
    medical_specialties: list[int]
    description: str
    
class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True