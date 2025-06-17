import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

class GeminiLLM:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        model_name = "gemini-1.5-flash-latest"
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model_name)

    def chat_with_tools(self, prompt: str, tools: list):
        response = self.client.generate_content(
            prompt,
            tools=tools
        )
        return response
