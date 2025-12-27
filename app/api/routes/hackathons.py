# api/routes/hackathons.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.hackathon import Hackathon
from app.schemas.hackathon import HackathonCreate

router = APIRouter(prefix="/hackathons", tags=["Hackathons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_hackathon(data: HackathonCreate, db: Session = Depends(get_db)):
    hackathon = Hackathon(**data.dict())
    db.add(hackathon)
    db.commit()
    db.refresh(hackathon)
    return hackathon

@router.get("/")
def list_hackathons(db: Session = Depends(get_db)):
    return db.query(Hackathon).all()

@router.get("/{hackathon_id}")
def get_hackathon(hackathon_id: int, db: Session = Depends(get_db)):
    return db.query(Hackathon).filter(Hackathon.id == hackathon_id).first()


@router.get("/")
def list_hackathons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Hackathon).offset(skip).limit(limit).all()
