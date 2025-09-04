from database import Base, engine, SessionLocal
from models import Profile, Skill, Project

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Seed profile
if not db.query(Profile).first():
    profile = Profile(
        name="Sachin Choudhary",
        email="sac072003@gmail.com",
        education="B.Tech Artificial Intelligence & Data Science",
        github="https://github.com/sachinchoudharyy",
        linkedin="https://www.linkedin.com/in/sachin-choudhary-83735b2a8/",
        # portfolio="https://yourportfolio.com"
    )
    db.add(profile)

# Seed skills
skills = [
    Skill(name="Python", level="Expert"),
    Skill(name="SQL", level="Intermediate"),
    Skill(name="Machine Learning", level="Intermediate"),
    Skill(name="Deep Learning", level="Intermediate"),
    Skill(name="Flask", level="Intermediate"),
    Skill(name="React", level="Beginner"),
    Skill(name="Computer Vision", level="Intermediate"),
    Skill(name="Web Scraping", level="Intermediate"),
    Skill(name="Natural Language Processing (NLP)", level="Intermediate"),
    Skill(name="Large Language Models (LLM)", level="Intermediate"),
    Skill(name="Retrieval-Augmented Generation (RAG)", level="Intermediate"),
    Skill(name="Data Analytics", level="Intermediate"),
    Skill(name="Generative AI", level="Beginner"),
    Skill(name="Data Engineering", level="Beginner")
]

for skill in skills:
    exists = db.query(Skill).filter_by(name=skill.name).first()
    if not exists:
        db.add(skill)

# Seed projects
projects = [
    Project(
        title="Vehicle Detection",
        description="Detects and counts vehicles in a video using YOLO.",
        link="https://github.com/yourusername/vehicle-detection",
        skill="Computer Vision"
    ),
    Project(
        title="Fertilizer Recommendation",
        description="Suggests fertilizer based on soil and crop data.",
        link="https://github.com/yourusername/fertilizer-recommendation",
        skill="Machine Learning"
    ),
    Project(
        title="Weekly Sales Prediction",
        description="Predicts supermarket sales using ML regression models.",
        link="https://github.com/yourusername/weekly-sales",
        skill="Data Analysis"
    ),
    Project(
        title="Number Plate Detection",
        description="Detects vehicle number plates from video feed.",
        link="https://github.com/yourusername/number-plate-detection",
        skill="OpenCV"
    ),
    Project(
        title="Shopping Cart Manager",
        description="OOP-based Python shopping cart management system.",
        link="https://github.com/yourusername/shopping-cart",
        skill="Python"
    ),
    Project(
        title="Web Scraping Doctors (Practo)",
        description="Scraped doctors’ info from Practo and stored in CSV.",
        link="https://github.com/yourusername/practo-scraper",
        skill="Web Scraping"
    ),
    Project(
        title="Chat with PDF (RAG-based)",
        description="Built a Retrieval-Augmented Generation (RAG) app to query PDFs using embeddings + LLM.",
        link="https://github.com/yourusername/chat-with-pdf",
        skill="LLM / RAG / NLP"
    ),
    Project(
        title="Diet Recommendation (LLM-powered)",
        description="LLM-based chatbot that provides personalized diet recommendations.",
        link="https://github.com/yourusername/diet-recommendation",
        skill="LLM / Generative AI"
    )
]

for project in projects:
    exists = db.query(Project).filter_by(title=project.title).first()
    if not exists:
        db.add(project)

db.commit()
db.close()

print("✅ Database seeded successfully without duplicates!")
