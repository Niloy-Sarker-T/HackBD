# schemas/submission.py
from pydantic import BaseModel

class SubmissionCreate(BaseModel):
    team_id: int
    project_name: str
    description: str
    github_link: str
    demo_link: str

from datetime import datetime
class SubmissionOut(SubmissionCreate):
    id: int
    status: str
    submitted_at: datetime

    class Config:
        orm_mode = True




class SubmissionOut(BaseModel):
    id: int
    project_name: str
    status: str
    submitted_at: datetime

    class Config:
        from_attributes = True
