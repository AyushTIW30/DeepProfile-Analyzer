from agent.signal_processor import detect_role_from_keywords, extract_skills_from_text

def summarize_generic(data):
    text = f"{data.get('title','')} {data.get('meta_description','')} {data.get('content','')}"
    role = detect_role_from_keywords(text)
    skills = extract_skills_from_text(text)

    summary = f"This profile appears to represent a {role}. "
    if skills:
        summary += f"Detected skills include: {', '.join(skills)}."

    return {
        "name": data.get("title"),
        "role": role,
        "skills": skills,
        "summary": summary
    }
