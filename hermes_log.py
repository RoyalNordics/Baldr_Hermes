# Logs communication between components

from datetime import datetime

def log(title, content):
    timestamp = datetime.now().isoformat()
    with open("ai-communication.md", "a", encoding="utf-8") as f:
        f.write(f"## {title} ({timestamp})\n{content}\n\n")