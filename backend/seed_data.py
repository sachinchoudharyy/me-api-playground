from database import Base, engine, SessionLocal
from models import Profile, Skill, Project

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Insert YOUR real data (replace with your info)
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
    Project(title="Vehicle Detection", description="Detects and counts vehicles in a video using YOLO.", link="https://github.com/yourusername/vehicle-detection", skill="Python"),
    Project(title="Fertilizer Recommendation", description="Suggests fertilizer based on soil and crop data.", link="https://github.com/yourusername/fertilizer-recommendation", skill="Machine Learning")
]
db.add_all(projects)

db.commit()
print("✅ Database seeded successfully!")
