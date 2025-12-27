# schemas/hackathon.py
from pydantic import BaseModel
from datetime import datetime

class HackathonCreate(BaseModel):
    title: str
    description: str
    host_id: int
    start_date: datetime
    end_date: datetime
    submission_deadline: datetime

class HackathonOut(HackathonCreate):
    id: int
