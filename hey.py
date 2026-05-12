import sys
import requests
import json

def ask_ollama(query):
    prompt = f"""You are a Linux shell expert. The user is on Ubuntu.
Return ONLY the shell command, nothing else. No explanation, no markdown, no backticks.

Task: {query}"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    result = response.json()
    return result["response"].strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: hey \"what you want to do\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    command = ask_ollama(query)
    print(command)
