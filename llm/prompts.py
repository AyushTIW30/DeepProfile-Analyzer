def build_profile_analysis_prompt(structured_data: dict) -> str:
    """
    Builds prompt to analyze structured profile data.
    """

    return f"""
You are an intelligent web profile analysis agent.

Analyze the following public profile data and return structured intelligence.

DATA:
{structured_data}

Tasks:
1. Identify full name (if available)
2. Detect platform type
3. Detect primary professional role (developer, manager, researcher, student, etc.)
4. Extract key skills
5. Extract projects
6. Extract achievements or awards
7. Summarize activity pattern
8. Provide confidence score between 0 and 1

Return output strictly in JSON format:

{{
  "name": "",
  "platform": "",
  "role_detected": "",
  "skills": [],
  "projects": [],
  "achievements": [],
  "activity_summary": "",
  "confidence_score": 0.0
}}
"""
