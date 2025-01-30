from datetime import datetime
from pydantic import BaseModel

class MedicalSpecialtiesBase(BaseModel):
    name: str
    description: str
    
class MedicalSpecialtiesCreate(MedicalSpecialtiesBase):
    pass

class MedicalSpecialtiesUpdate(MedicalSpecialtiesBase):
    pass

class MedicalSpecialties(MedicalSpecialtiesBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True