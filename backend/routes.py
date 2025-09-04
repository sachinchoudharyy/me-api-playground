# from flask import Blueprint, request
# from database import SessionLocal
# from models import Profile, Skill, Project


# api = Blueprint("api", __name__)
# db = SessionLocal()

# @api.route("/profile", methods=["GET"])
# def get_profile():
#     profile = db.query(Profile).first()
#     if profile:
#         return {
#             "name": profile.name,
#             "email": profile.email,
#             "education": profile.education,
#             "github": profile.github,
#             "linkedin": profile.linkedin,
#             "portfolio": profile.portfolio
#         }
#     return {"error": "Profile not found"}, 404

# @api.route("/skills/top", methods=["GET"])
# def get_skills():
#     skills = db.query(Skill).all()
#     return [{"name": s.name, "level": s.level} for s in skills]


# @api.route("/search", methods=["GET"])
# def search():
#     q = (request.args.get("q") or "").strip().lower()
#     results = []

#     if q:
#         projects = db.query(Project).filter(
#             Project.title.ilike(f"%{q}%") |
#             Project.description.ilike(f"%{q}%") |
#             Project.skill.ilike(f"%{q}%")
#         ).all()
#         results = [{
#             "title": p.title,
#             "description": p.description,
#             "link": p.link,
#             "skill": p.skill
#         } for p in projects]

#     return results


# @api.route("/projects", methods=["GET"])
# def get_projects():
#     skill = request.args.get("skill")
#     query = db.query(Project)
#     if skill:
#         query = query.filter(Project.skill.ilike(f"%{skill}%"))
#     projects = query.all()
#     return [{"title": p.title, "description": p.description, "link": p.link, "skill": p.skill} for p in projects]
# routes.py
from flask import Blueprint, request
from database import SessionLocal
from models import Profile, Skill, Project

# NOTE: no url_prefix here so endpoints are exactly /profile, /projects, /skills, /skills/top, /search
api = Blueprint("api", __name__)

def get_db():
    return SessionLocal()

@api.route("/profile", methods=["GET"])
def get_profile():
    db = get_db()
    try:
        p = db.query(Profile).first()
        if not p:
            return {"error": "Profile not found"}, 404
        return {
            "name": p.name,
            "email": p.email,
            "education": p.education,
            "github": p.github,
            "linkedin": p.linkedin,
            "portfolio": p.portfolio
        }, 200
    finally:
        db.close()

@api.route("/projects", methods=["GET"])
def get_projects():
    db = get_db()
    try:
        skill = request.args.get("skill")
        q = db.query(Project)
        if skill:
            q = q.filter(Project.skill.ilike(f"%{skill}%"))
        items = q.all()
        return [
            {"title": x.title, "description": x.description, "link": x.link, "skill": x.skill}
            for x in items
        ], 200
    finally:
        db.close()

# --- Skills endpoints (both /skills and /skills/top return the same) ---
@api.route("/skills", methods=["GET"])
def get_skills_plain():
    return _get_skills_impl()

@api.route("/skills/top", methods=["GET"])
def get_skills_top():
    return _get_skills_impl()

def _get_skills_impl():
    db = get_db()
    try:
        items = db.query(Skill).all()
        return [
            {"name": s.name, "level": s.level if s.level else ""}
            for s in items
        ], 200
    finally:
        db.close()

# --- Optional search used by UI ---
@api.route("/search", methods=["GET"])
def search():
    db = get_db()
    try:
        q = (request.args.get("q") or "").strip()
        if not q:
            return [], 200
        rows = db.query(Project).filter(
            (Project.title.ilike(f"%{q}%")) |
            (Project.description.ilike(f"%{q}%")) |
            (Project.skill.ilike(f"%{q}%"))
        ).all()
        return [
            {"title": p.title, "description": p.description, "link": p.link, "skill": p.skill}
            for p in rows
        ], 200
    finally:
        db.close()
