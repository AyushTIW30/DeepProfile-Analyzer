from llm.ollama_client import generate_json_response
from llm.prompts import build_profile_analysis_prompt


def analyze_profile(structured_data: dict):
    prompt = build_profile_analysis_prompt(structured_data)
    return generate_json_response(prompt)
