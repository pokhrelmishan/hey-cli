# hey 🤖

A local AI-powered terminal assistant that converts natural language to shell commands.

## Demo

$ hey "show disk usage"
df -h

$ hey "kill the process using port 8080"
ps aux | grep 8080 | awk '{print $2}' | xargs kill -9

## Installation

1. Install Ollama from https://ollama.com
2. Run: ollama pull llama3.2
3. Clone this repo and run: sudo cp hey.py /usr/local/bin/hey

## Requirements
- Python 3
- Ollama
- pip install requests
