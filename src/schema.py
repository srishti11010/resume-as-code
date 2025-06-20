from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class Experience(BaseModel):
    company: str
    position: str
    start: str
    end: Optional[str]
    description: Optional[str]

class Education(BaseModel):
    degree: str
    institution: str
    year: Optional[str]

class Resume(BaseModel):
    name: str
    title: Optional[str]
    contact_email: Optional[EmailStr]
    github: Optional[str]
    website: Optional[str]
    experience: Optional[List[Experience]]
    education: Optional[List[Education]]
    skills: Optional[List[str]]

    # Example validation if needed
    @validator('experience', each_item=True)
    def check_experience_dates(cls, v):
        # Add checks here if needed
        return v
