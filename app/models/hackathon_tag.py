from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

hackathon_tags = Table(
    "hackathon_tags",
    Base.metadata,
    Column("hackathon_id", Integer, ForeignKey("hackathons.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)
