def detect_role_from_keywords(text):
    text = text.lower()

    if any(word in text for word in ["python", "django", "fastapi", "api", "backend"]):
        return "Backend Developer"
    if any(word in text for word in ["react", "frontend", "ui", "css", "javascript"]):
        return "Frontend Developer"
    if any(word in text for word in ["machine learning", "model", "pandas", "ml"]):
        return "Machine Learning Engineer"
    if any(word in text for word in ["management", "strategy", "kpi", "roadmap"]):
        return "Management Professional"

    return "General Professional"

def extract_skills_from_text(text):
    skills = []
    keywords = [
        "python", "javascript", "react", "django", "fastapi",
        "sql", "machine learning", "tensorflow", "api"
    ]
    text_lower = text.lower()

    for skill in keywords:
        if skill in text_lower:
            skills.append(skill.title())

    return list(set(skills))
