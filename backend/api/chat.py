from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from core.vectorstore import similarity_search
from core.rag import build_prompt
from core.gemini import GeminiClient
import asyncio

router = APIRouter(prefix="/chat")

gemini = GeminiClient()

class ChatRequest(BaseModel):
    query: str

async def fake_stream(text: str):
    for word in text.split():
        yield word + " "
        await asyncio.sleep(0.04)

@router.post("/")
async def chat(req: ChatRequest):
    query_embedding = await gemini.embed(req.query)
    contexts = await similarity_search(query_embedding, k=5)

    prompt = build_prompt(req.query, contexts)
    answer = await gemini.generate(prompt)

    return StreamingResponse(fake_stream(answer), media_type="text/plain")
