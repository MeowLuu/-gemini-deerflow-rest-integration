import os
from pathlib import Path

BASE_DIR = Path("test_files")

def list_files() -> list[str]:
    """List all files under test_files directory."""
    files = []
    for file in BASE_DIR.rglob("*"):
        if file.is_file():
            files.append(file.name)
    return files

def read_file(name: str) -> str:
    """Read content of a file."""
    try:
        with open(BASE_DIR / name, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"