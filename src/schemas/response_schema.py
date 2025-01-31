from pydantic import BaseModel, HttpUrl
from typing import List, Union, Optional
from .doctor_schemas import Doctor
from .medical_specialties_schemas import MedicalSpecialties

class ResponseSchema(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    next_page: Optional[HttpUrl] = None
    previous_page: Optional[HttpUrl] = None
    items: List[Union[Doctor, MedicalSpecialties]]
    