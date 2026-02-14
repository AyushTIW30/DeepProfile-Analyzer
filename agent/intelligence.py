from llm.ollama_client import generate_json_response


def generate_leetcode_intelligence(profile_data: dict):
    prompt = f"""
You are a senior technical hiring analyst.

Perform a deep structured performance evaluation.

PROFILE DATA:
{profile_data}

Analyze with detailed reasoning:

1. Compare difficulty distribution ratio.
2. Infer algorithmic maturity level.
3. Estimate DSA depth.
4. Evaluate competitiveness for FAANG-level roles.
5. Provide improvement roadmap with milestones.
6. Give confidence score based on data completeness.

Return strictly JSON:

{{
  "overall_level": "",
  "strength_analysis": "",
  "weakness_analysis": "",
  "improvement_suggestions": [],
  "career_alignment": "",
  "confidence_score": 0.0
}}
"""
    return generate_json_response(prompt)


def format_leetcode_report(basic_profile: dict, ai_data: dict) -> str:
    report = f"""
🧑 Profile Summary
Name: {basic_profile.get("name")}
Username: {basic_profile.get("username")}
Ranking: {basic_profile.get("ranking")}
Total Problems Solved: {basic_profile.get("total_solved")}

Difficulty Breakdown:
   - Easy: {basic_profile.get("easy")}
   - Medium: {basic_profile.get("medium")}
   - Hard: {basic_profile.get("hard")}

────────────────────────────

📊 Performance Evaluation
Overall Level: {ai_data.get("overall_level")}

Strength Analysis:
{ai_data.get("strength_analysis")}

Weakness Analysis:
{ai_data.get("weakness_analysis")}

Career Alignment:
{ai_data.get("career_alignment")}

────────────────────────────

🚀 Improvement Roadmap:
"""

    suggestions = ai_data.get("improvement_suggestions", [])

    for item in suggestions:
        if isinstance(item, dict):
            report += f"\n• {item.get('milestone')}: {item.get('goal')}"
        else:
            report += f"\n• {item}"

    report += f"\n\nConfidence Score: {ai_data.get('confidence_score')}\n"

    return report
