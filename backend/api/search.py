from fastapi import APIRouter
from core.embeddings import EmbeddingClient
from core.vectorstore import similarity_search
from core.rag import build_prompt
from core.gemini import GeminiClient

router = APIRouter(prefix="/chat")

embedder = EmbeddingClient()
gemini = GeminiClient()

@router.post("/")
async def chat(query: str):
    query_embedding = await embedder.embed(query)
    contexts = await similarity_search(query_embedding, k=5)

    prompt = build_prompt(query, contexts)
    response = await gemini.generate(prompt)

    return {
        "answer": response,
        "sources": contexts
    }
