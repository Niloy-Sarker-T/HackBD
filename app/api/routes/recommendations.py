from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.student import Student
from app.models.hackathon import Hackathon

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/students/{student_id}")
def recommend_hackathons(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).get(student_id)
    if not student:
        return []

    student_tag_ids = {tag.id for tag in student.interests}

    results = []

    for hackathon in db.query(Hackathon).all():
        score = 0
        for tag in hackathon.tags:
            if tag.id in student_tag_ids:
                score += tag.weight   # 🔥 weighted score

        if score > 0:
            results.append({
                "hackathon_id": hackathon.id,
                "title": hackathon.title,
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
