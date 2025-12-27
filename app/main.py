# main.py
from fastapi import FastAPI
from app.api.router import router
from app.db.base import Base
from app.db.session import engine

# 🔥 IMPORT ALL MODELS (IMPORTANT)
from app.models.hackathon import Hackathon
from app.models.team import Team
from app.models.submission import Submission
from app.models.tag import Tag
from app.models.student import Student  # if exists
from app.models.user import User
from app.db.seed import seed_tags
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, BD Hackathons!"}

app.include_router(router)
