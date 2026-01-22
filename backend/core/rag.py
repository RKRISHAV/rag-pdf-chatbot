from core.gemini import GeminiClient

gemini = GeminiClient()

def build_prompt(query, contexts):
    joined = "\n\n".join(
        [f"[Source {i+1}]: {c['content']}" for i, c in enumerate(contexts)]
    )

    return f"""
You are a factual assistant. Answer ONLY using the sources below.
If the answer is not in the sources, say: "I don't know."

SOURCES:
{joined}

QUESTION:
{query}

Answer with citations like: (Source 1), (Source 2).
"""
