@router.patch("/{submission_id}/finalize")
def finalize_submission(submission_id: int, db: Session = Depends(get_db)):

    submission = db.query(Submission).filter(
        Submission.id == submission_id
    ).first()

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    # Mark other submissions inactive
    db.query(Submission).filter(
        Submission.team_id == submission.team_id,
        Submission.id != submission_id
    ).update({"status": "inactive"})

    submission.status = "final"
    db.commit()

    return {"message": "Submission marked as final"}
