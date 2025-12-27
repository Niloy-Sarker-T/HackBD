from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.student import Student
from app.models.tag import Tag
from app.schemas.student import StudentCreate

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    tags = db.query(Tag).filter(Tag.id.in_(data.interest_tag_ids)).all()

    student = Student(
        name=data.name,
        university=data.university,
        year=data.year,
        interests=tags
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
