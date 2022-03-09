from typing import List, Optional
from unicodedata import category
from pydantic import BaseModel
from datetime import date


class Refugee(BaseModel):
    id: int
    first_name: str
    family_name: str
    birth_date: Optional[date] = None
    salary_targeted: Optional[int] = None
    email: str
    keywords: str

    class Config:
        orm_mode = True

class EquivalentKeyword(BaseModel):
    label: str
    keyword: str

    class Config:
        orm_mode = True

class Keyword(BaseModel):
    label: str
    # category: Optional[str]

    class Config:
        orm_mode = True
