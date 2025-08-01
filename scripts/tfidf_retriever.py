import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === Step 1: Load chunked data ===
with open("data/book_chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n\n")  # Each chunk separated by blank line

# === Step 2: Vectorize using TF-IDF ===
vectorizer = TfidfVectorizer()
chunk_vectors = vectorizer.fit_transform(chunks)

# === Step 3: Ask user question ===
print("\n🧠 LMIS Bot is ready! Ask your AIML interview questions.\nType 'exit' to quit.\n")

while True:
    query = input("❓ You: ").strip()
    if query.lower() == "exit":
        print("👋 Goodbye!")
        break

    # === Step 4: Vectorize the query ===
    query_vector = vectorizer.transform([query])

    # === Step 5: Compute similarity ===
    similarity_scores = cosine_similarity(query_vector, chunk_vectors)
    top_index = similarity_scores[0].argmax()
    top_score = similarity_scores[0][top_index]
    top_chunk = chunks[top_index]

    # === Step 6: Show result ===
    print(f"\n🟩 Top Match (Score: {top_score:.2f}):\n")
    print(top_chunk)
    print("-" * 80)
