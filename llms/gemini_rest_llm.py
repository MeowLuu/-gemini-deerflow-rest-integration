import os
import requests
import yaml


with open("conf.yaml", "r") as f:
    config = yaml.safe_load(f)

class GeminiRestLLM:
    def __init__(self):
        self.api_key = config["GEMINI_API_KEY"]
        self.api_url = config["API_URL"]
        self.headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key
        }

    def chat(self, user_input, tool_schemas):
        """Call Gemini REST API"""
        payload = {
            "contents": [{"role": "user", "parts": [{"text": user_input}]}],
            "tools": [{"function_declarations": tool_schemas}]
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.json()