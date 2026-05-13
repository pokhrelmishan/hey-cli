#!/usr/bin/env python3
import sys
import requests

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def ask_ollama(query):
    prompt = f"""You are a Linux shell expert. The user is on Ubuntu.
Return ONLY the shell command, nothing else. No explanation, no markdown, no backticks.

Task: {query}"""

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }, timeout=30)
        result = response.json()
        return result["response"].strip()
    except requests.exceptions.ConnectionError:
        print(f"{RED}❌ Ollama is not running. Start it with: ollama serve{RESET}")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"{RED}❌ Ollama timed out. Try again.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: hey \"what you want to do\"")
        print(f"Example: hey \"show disk usage\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    command = ask_ollama(query)
    print(f"{GREEN}{command}{RESET}")