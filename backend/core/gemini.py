import httpx
from core.config import GEMINI_API_KEY

class GeminiClient:
    def __init__(self):
        self.generate_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        self.embed_url = "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent"

    async def generate(self, prompt: str):
        headers = {"Content-Type": "application/json"}
        params = {"key": GEMINI_API_KEY}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(self.generate_url, headers=headers, params=params, json=payload)
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]

    async def embed(self, text: str):
        headers = {"Content-Type": "application/json"}
        params = {"key": GEMINI_API_KEY}
        payload = {
            "content": {
                "parts": [{"text": text}]
            }
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(self.embed_url, headers=headers, params=params, json=payload)
            data = res.json()
            return data["embedding"]["values"]
