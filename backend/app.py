import os
from flask import Flask
from flask_cors import CORS
from routes import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

from database import Base, engine, SessionLocal
from models import Profile, Skill, Project

def init_db():
    Base.metadata.create_all(bind=engine)  # create tables if missing
    db = SessionLocal()

    # only seed if empty
    if not db.query(Profile).first():
        profile = Profile(
            name="Sachin Choudhary",
            email="your.email@example.com",
            education="B.Tech Artificial Intelligence & Data Science",
            github="https://github.com/yourusername",
            linkedin="https://linkedin.com/in/yourprofile",
            portfolio="https://yourportfolio.com"
        )
        db.add(profile)

        skills = [
            Skill(name="Python", level="Expert"),
            Skill(name="SQL", level="Intermediate"),
            Skill(name="Machine Learning", level="Intermediate")
        ]
        db.add_all(skills)

        projects = [
            Project(
                title="Vehicle Detection",
                description="Detects and counts vehicles in a video using YOLO.",
                link="https://github.com/yourusername/vehicle-detection",
                skill="Python"
            ),
            Project(
                title="Fertilizer Recommendation",
                description="Suggests fertilizer based on soil and crop data.",
                link="https://github.com/yourusername/fertilizer-recommendation",
                skill="Machine Learning"
            )
        ]
        db.add_all(projects)

        db.commit()
    db.close()

# Initialize DB when app starts
init_db()



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets port dynamically
    app.run(host="0.0.0.0", port=port)

