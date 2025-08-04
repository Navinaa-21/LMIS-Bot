import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === Step 0: Download NLTK Resources ===
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))

# === Step 1: Load chunked book data ===
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

# === Step 2: Preprocessing function ===
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)      # Remove digits
    words = word_tokenize(text, preserve_line=True)
    tokens = [word for word in words if word not in stop_words]
    return ' '.join(tokens)

# === Step 3: Preprocess all chunks ===
processed_chunks = [preprocess(chunk) for chunk in raw_chunks]

# === Step 4: Vectorize chunks using TF-IDF ===
vectorizer = TfidfVectorizer(ngram_range=(1, 2))  # unigrams + bigrams
chunk_vectors = vectorizer.fit_transform(processed_chunks)

# === Step 5: Define Q&A logic ===
def ask_question(query):
    cleaned_query = preprocess(query)
    query_vector = vectorizer.transform([cleaned_query])
    similarity_scores = cosine_similarity(query_vector, chunk_vectors)
    top_index = similarity_scores[0].argmax()
    top_score = similarity_scores[0][top_index]
    best_chunk = raw_chunks[top_index]  # Return original for readability
    return best_chunk, top_score

# === Step 6: Start interaction ===
print("\n🧠 LMIS Bot is ready! Ask your AIML interview questions.\nType 'exit' to quit.\n")

try:
    while True:
        query = input("❓ You: ").strip()
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break
        if not query:
            print("⚠️ Please enter a valid question.")
            continue

        answer, score = ask_question(query)
        print(f"\n🟩 Top Match (Score: {score:.2f}):\n")
        print(answer)
        print("-" * 80)

except KeyboardInterrupt:
    print("\n👋 Session ended by user.")
