import os

def setup_directories():
    os.makedirs("assets/css", exist_ok=True)
    os.makedirs("assets/img", exist_ok=True)
    os.makedirs("projects", exist_ok=True)

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
