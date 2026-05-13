

## Preview

[![asciicast]([https://asciinema.org/a/hOJEQnDvwxOuHNv7.svg)](https://asciinema.org/a/hOJEQnDvwxOuHNv7)](https://asciinema.org/a/hOJEQnDvwxOuHNv7.svg)](https://asciinema.org/a/hOJEQnDvwxOuHNv7))

# hey 🤖

A local AI-powered terminal assistant that converts natural language to shell commands. Runs 100% locally — no API key, no internet required.

## Demo

```bash
$ hey "show disk usage"
df -h

$ hey "kill the process using port 8080"
ps aux | grep 8080 | awk '{print $2}' | xargs kill -9

$ hey "find all python files modified in the last 7 days"
find . -type f -name "*.py" -mtime +7
```

## Requirements

- Python 3
- [Ollama](https://ollama.com) installed and running

## Installation

```bash
# 1. Install Ollama and pull the model
ollama pull llama3.2

# 2. Install requests
pip install requests

# 3. Clone and install
git clone https://github.com/pokhrelmishan/hey-cli.git
cd hey-cli
sudo cp hey.py /usr/local/bin/hey

# 4. Use it
hey "your query here"
```

## Why hey?

- No API key needed
- Works offline
- Fast — powered by Llama 3.2 running locally
- Linux/Ubuntu focused

## Author

Built by [@pokhrelmishan](https://github.com/pokhrelmishan)