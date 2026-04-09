from rag.vectorstore import get_collection


def retrieve(query: str, user_type: str, top_k: int = 2) -> list[dict]:
    collection = get_collection()

    def _query(where: dict | None) -> list[dict]:
        kwargs = dict(query_texts=[query], n_results=top_k)
        if where:
            kwargs["where"] = where
        results = collection.query(**kwargs)
        chunks = []
        if results and results["metadatas"]:
            for meta, distance in zip(results["metadatas"][0], results["distances"][0]):
                chunks.append({
                    "question": meta.get("question", ""),
                    "answer": meta.get("answer", ""),
                    "category": meta.get("category", ""),
                    "score": distance,
                })
        return chunks

    # Search 1: filtered by user_type
    typed_chunks = _query({"user_type": user_type})

    # Search 2: no filter (community + all types)
    all_chunks = _query(None)

    # Merge, deduplicate by question text, typed results first
    seen = set()
    merged = []
    for chunk in typed_chunks + all_chunks:
        key = chunk["question"]
        if key not in seen:
            seen.add(key)
            merged.append(chunk)

    return merged
