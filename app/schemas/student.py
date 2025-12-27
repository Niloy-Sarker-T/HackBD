from pydantic import BaseModel
from typing import List

class StudentCreate(BaseModel):
    name: str
    university: str
    year: int
    interest_tag_ids: List[int]
