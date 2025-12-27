from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Table, ForeignKey

from app.models.hackathon_tag import hackathon_tags


hackathon_tags = Table(
    "hackathon_tags",
    Base.metadata,
    Column("hackathon_id", ForeignKey("hackathons.id")),
    Column("tag_id", ForeignKey("tags.id")),
)

class Hackathon(Base):
    __tablename__ = "hackathons"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    host_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    submission_deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    teams = relationship("Team", back_populates="hackathon")
    tags = relationship(
        "Tag",
        secondary=hackathon_tags,
        back_populates="hackathons"
    )