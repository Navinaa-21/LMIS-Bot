# scripts/semantic_retriever.py

import os
from sentence_transformers import SentenceTransformer, util

# === Load chunked text ===
CHUNK_PATH = "data/book_chunks.txt"

def load_chunks(path):
    if not os.path.exists(path):
        print(f"❌ Error: '{path}' not found.")
        exit(1)
    with open(path, "r", encoding="utf-8") as f:
        chunks = f.read().split("\n\n")
    print(f"✅ Loaded {len(chunks)} chunks from book.")
    return chunks

raw_chunks = load_chunks(CHUNK_PATH)

# === Load semantic QA model ===
print("📦 Loading model...")
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

# === Encode all chunks ===
print("🔍 Embedding chunks...")
chunk_embeddings = model.encode(raw_chunks, convert_to_tensor=True)

# === Interactive Q&A ===
print("\n🧠 LMIS Bot (Semantic Mode) is ready! Ask your AIML interview questions.\nType 'exit' to quit.\n")

while True:
    query = input("❓ You: ").strip()
    if query.lower() == "exit":
        print("👋 Goodbye!")
        break
    if not query:
        print("⚠️ Please enter a valid question.")
        continue

    query_embedding = model.encode(query, convert_to_tensor=True)
    similarity_scores = util.cos_sim(query_embedding, chunk_embeddings)
    top_idx = similarity_scores.argmax().item()
    top_score = similarity_scores[0][top_idx].item()
    top_chunk = raw_chunks[top_idx]

    print(f"\n🟩 Top Match (Score: {top_score:.2f}):\n")
    print(top_chunk)
    print("-" * 80)
