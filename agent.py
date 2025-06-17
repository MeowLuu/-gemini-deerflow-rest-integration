import os
import yaml
import json
import requests
from dotenv import load_dotenv

from deerflow.tools import tools

# Load environment variables and config
load_dotenv()
with open("conf.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["GEMINI_API_KEY"]
API_URL = config["API_URL"]

# Set headers for Gemini REST API call
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

# Define function calling tool schema (function declarations)
function_declarations = [
    {
        "name": "list_files",
        "description": "List all files in working directory",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "read_file",
        "description": "Read content of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "File name to read"}
            },
            "required": ["name"]
        }
    }
]

# Main agent loop
while True:
    user_input = input("User: ")

    # Construct request payload
    data = {
        "contents": [{"role": "user", "parts": [{"text": user_input}]}],
        "tools": [{"function_declarations": function_declarations}]
    }

    # Make Gemini REST API call
    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()

    candidate = result["candidates"][0]
    part = candidate["content"]["parts"][0]

    # Check if Gemini called a function/tool
    if "functionCall" in part:
        fn = part["functionCall"]["name"]
        args = part["functionCall"]["args"]

        print(f"Gemini calls: {fn} with args: {args}")

        # Dispatch to actual Python functions
        if fn == "list_files":
            tool_result = tools.list_files()
        elif fn == "read_file":
            tool_result = tools.read_file(args["name"])
        else:
            tool_result = "Unknown tool"

        print("Tool Result:", tool_result)

    elif "text" in part:
        print("Gemini text:", part["text"])