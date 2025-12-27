# api/routes/teams.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.team import Team
from app.schemas.team import TeamCreate

router = APIRouter(prefix="/teams", tags=["Teams"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_team(data: TeamCreate, db: Session = Depends(get_db)):
    team = Team(**data.dict())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

@router.get("/hackathon/{hackathon_id}")
def get_teams_by_hackathon(hackathon_id: int, db: Session = Depends(get_db)):
    return db.query(Team).filter(Team.hackathon_id == hackathon_id).all()
