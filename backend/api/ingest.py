from fastapi import APIRouter, UploadFile, File
from core.pdf import extract_text_from_pdf
from core.chunking import chunk_text
from core.gemini import GeminiClient
from core.vectorstore import store_embedding

router = APIRouter(prefix="/ingest")

gemini = GeminiClient()

@router.post("/pdf")
async def ingest_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = await gemini.embed(chunk)
        await store_embedding(chunk, embedding)

    return {"status": "success", "chunks": len(chunks)}
