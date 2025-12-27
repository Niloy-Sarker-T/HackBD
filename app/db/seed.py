from sqlalchemy.orm import Session
from app.models.tag import Tag

DEFAULT_TAGS = [
    "AI",
    "Web",
    "Blockchain",
    "IoT",
    "Data Science",
    "Mobile",
    "Cybersecurity",
]

def seed_tags(db: Session):
    for tag_name in DEFAULT_TAGS:
        exists = db.query(Tag).filter(Tag.name == tag_name).first()
        if not exists:
            db.add(Tag(name=tag_name))
    db.commit()
