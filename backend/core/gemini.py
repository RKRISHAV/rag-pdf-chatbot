import httpx
from core.config import GEMINI_API_KEY

class GeminiClient:
    def __init__(self):
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    async def generate(self, prompt: str):
        headers = {"Content-Type": "application/json"}
        params = {"key": GEMINI_API_KEY}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, headers=headers, params=params, json=payload)
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
