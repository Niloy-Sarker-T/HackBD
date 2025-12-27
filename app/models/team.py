# models/team.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hackathon_id = Column(Integer, ForeignKey("hackathons.id"))
    leader_id = Column(Integer)

    hackathon = relationship("Hackathon", back_populates="teams")
    submissions = relationship("Submission", back_populates="team")

