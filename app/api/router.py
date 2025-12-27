from fastapi import APIRouter
from app.api.routes import hackathons, teams, submissions, students, recommendations

router = APIRouter()

router.include_router(hackathons.router)
router.include_router(teams.router)
router.include_router(submissions.router)
router.include_router(students.router)
router.include_router(recommendations.router)
