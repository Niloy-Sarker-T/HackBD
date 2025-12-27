from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

student_tags = Table(
    "student_tags",
    Base.metadata,
    Column("student_id", ForeignKey("students.id")),
    Column("tag_id", ForeignKey("tags.id")),
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    university = Column(String)
    year = Column(Integer)

    interests = relationship("Tag", secondary=student_tags)
