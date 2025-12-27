from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.submission import Submission
from app.schemas.submission import SubmissionCreate, SubmissionOut
from typing import List

router = APIRouter(prefix="/submissions", tags=["Submissions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SubmissionOut)
def submit_project(data: SubmissionCreate, db: Session = Depends(get_db)):

    # 1️⃣ Find active/final submission
    previous = db.query(Submission).filter(
        Submission.team_id == data.team_id,
        Submission.status != "inactive"
    ).all()

    # 2️⃣ Mark them inactive
    for sub in previous:
        sub.status = "inactive"

    # 3️⃣ Create new submission
    new_submission = Submission(
        **data.dict(),
        status="submitted"
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission
@router.get("/team/{team_id}")
def get_team_submissions(team_id: int, db: Session = Depends(get_db)):
    return db.query(Submission).filter(Submission.team_id == team_id).all()


from fastapi import HTTPException
from datetime import datetime
from app.models.team import Team

@router.post("/")
def submit_project(data: SubmissionCreate, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == data.team_id).first()

    if datetime.utcnow() > team.hackathon.submission_deadline:
        raise HTTPException(status_code=400, detail="Submission deadline passed")

    submission = Submission(**data.dict())
    db.add(submission)
    db.commit()
    return submission


@router.put("/{submission_id}")
def update_submission(submission_id: int, data: SubmissionCreate, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Not found")

    for key, value in data.dict().items():
        setattr(submission, key, value)

    db.commit()
    return submission


@router.delete("/{submission_id}")
def delete_submission(submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404)

    db.delete(submission)
    db.commit()
    return {"message": "Deleted"}


@router.patch("/{submission_id}/finalize")
def finalize_submission(submission_id: int, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()

    if not submission:
        raise HTTPException(status_code=404, detail="Not found")

    db.query(Submission).filter(
        Submission.team_id == submission.team_id,
        Submission.id != submission_id
    ).update({"status": "inactive"})

    submission.status = "final"
    db.commit()

    return {"message": "Final submission locked"}

