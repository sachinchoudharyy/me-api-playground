from flask import Blueprint, request
from database import SessionLocal
from models import Profile, Skill, Project

api = Blueprint("api", __name__)
db = SessionLocal()

@api.route("/profile", methods=["GET"])
def get_profile():
    profile = db.query(Profile).first()
    if profile:
        return {
            "name": profile.name,
            "email": profile.email,
            "education": profile.education,
            "github": profile.github,
            "linkedin": profile.linkedin,
            "portfolio": profile.portfolio
        }
    return {"error": "Profile not found"}, 404

@api.route("/projects", methods=["GET"])
def get_projects():
    skill = request.args.get("skill")
    query = db.query(Project)
    if skill:
        query = query.filter(Project.skill.ilike(f"%{skill}%"))
    projects = query.all()
    return [{"title": p.title, "description": p.description, "link": p.link, "skill": p.skill} for p in projects]
