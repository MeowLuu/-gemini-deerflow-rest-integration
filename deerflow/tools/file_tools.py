import os
from pathlib import Path

BASE_DIR = Path("./test_files")

def list_files() -> list[str]:
    """List all files under the test_files directory"""
    files = []
    for file in BASE_DIR.rglob("*"):
        if file.is_file():
            files.append(file.name)
    return files

def read_file(name: str) -> str:
    """Read file content"""
    try:
        with open(BASE_DIR / name, "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"