import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  # change to llama3 if you prefer


def generate_response(prompt: str, temperature: float = 0.2) -> str:
    """
    Sends prompt to local Ollama model and returns response text.
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"


def generate_json_response(prompt: str, temperature: float = 0.1) -> dict:
    """
    Forces strict JSON output from LLM.
    """

    strict_prompt = f"""
You must return ONLY valid JSON.
No markdown.
No explanation.
No backticks.
No extra text.

Follow this schema strictly.

{prompt}
"""

    response_text = generate_response(strict_prompt, temperature)

    # Clean common formatting issues
    cleaned = response_text.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except Exception:
        return {
            "error": "Invalid JSON from LLM",
            "raw_output": cleaned
        }
