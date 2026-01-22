from supabase import create_client
from core.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def store_embedding(content, embedding):
    supabase.table("documents").insert({
        "content": content,
        "embedding": embedding
    }).execute()

async def similarity_search(query_embedding, k=5):
    res = supabase.rpc("match_documents", {
        "query_embedding": query_embedding,
        "match_count": k
    }).execute()
    return res.data
