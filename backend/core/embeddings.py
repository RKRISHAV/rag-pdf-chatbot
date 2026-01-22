import httpx
from core.config import HF_API_KEY

class EmbeddingClient:
    def __init__(self):
        self.url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
        self.headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    async def embed(self, text: str):
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, headers=self.headers, json={"inputs": text})
            return res.json()
