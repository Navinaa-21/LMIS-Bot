# scripts/app.py

from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import os

app = Flask(__name__)

# Load model and data
print("🔧 Loading model and data...")
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

with open("data/book_chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n\n")

chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
print(f"✅ Loaded {len(chunks)} chunks.")


@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Embed question
    query_embedding = model.encode(question, convert_to_tensor=True)
    similarity_scores = util.cos_sim(query_embedding, chunk_embeddings)
    top_idx = similarity_scores.argmax().item()
    top_score = similarity_scores[0][top_idx].item()
    top_chunk = chunks[top_idx]

    return jsonify({
        "question": question,
        "answer": top_chunk,
        "score": round(top_score, 2)
    })


@app.route("/", methods=["GET"])
def home():
    return "✅ LMIS Bot Backend is running."


if __name__ == "__main__":
    app.run(debug=True)
