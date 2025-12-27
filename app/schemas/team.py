# schemas/team.py
from pydantic import BaseModel

class TeamCreate(BaseModel):
    name: str
    hackathon_id: int
    leader_id: int
