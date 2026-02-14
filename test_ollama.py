from llm.ollama_client import generate_response

response = generate_response("Say hello in one short sentence.")
print("MODEL RESPONSE:")
print(response)
