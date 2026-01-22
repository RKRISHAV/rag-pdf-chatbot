from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from core.embeddings import EmbeddingClient
from core.vectorstore import similarity_search
from core.rag import build_prompt
from core.gemini import GeminiClient
import asyncio

router = APIRouter(prefix="/chat")

embedder = EmbeddingClient()
gemini = GeminiClient()

async def fake_stream(text: str):
    for word in text.split():
        yield word + " "
        await asyncio.sleep(0.05)

@router.post("/")
async def chat(query: str):
    query_embedding = await embedder.embed(query)
    contexts = await similarity_search(query_embedding, k=5)

    prompt = build_prompt(query, contexts)
    answer = await gemini.generate(prompt)

    return StreamingResponse(
        fake_stream(answer),
        media_type="text/plain"
    )
