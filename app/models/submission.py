from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    project_name = Column(String)
    description = Column(Text)
    github_link = Column(String)
    demo_link = Column(String)
    status = Column(String, default="draft")  # draft | final | inactive
    submitted_at = Column(DateTime, default=datetime.utcnow)

    team = relationship("Team", back_populates="submissions")
