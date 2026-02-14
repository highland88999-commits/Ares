import requests
import json

def ask_ares_brain(log_snippet):
    """Sends a log snippet to the local AI for a verdict."""
    prompt = f"""
    Analyze this server log entry for malicious intent (scrapers, SQLi, brute force, or path traversal).
    Log: {log_snippet}
    
    If it is an attack, respond with exactly 'VOID'. 
    If it is a normal user or bot, respond with 'PASS'.
    Verdict:"""

    try:
        response = requests.post('http://localhost:11434/api/generate', 
            json={
                "model": "mistral", # or "llama3"
                "prompt": prompt,
                "stream": False
            })
        result = response.json().get('response', 'PASS').strip().upper()
        return "VOID" in result
    except Exception as e:
        print(f"ARES BRAIN ERROR: {e}")
        return False # Fail safe
