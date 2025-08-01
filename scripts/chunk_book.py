import fitz  # PyMuPDF
import os
import re

# === Step 1: Load PDF and extract text ===
pdf_file = "data/book.pdf"  # Make sure your PDF is inside the 'data' folder
doc = fitz.open(pdf_file)

full_text = ""
for page in doc:
    full_text += page.get_text()

# === Step 2: Clean the text ===
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)         # Remove multiple newlines
    text = re.sub(r'\s+', ' ', text)          # Remove extra spaces
    text = text.replace('\xa0', ' ')          # Replace non-breaking spaces
    return text.strip()

cleaned_text = clean_text(full_text)

# ✅ Ensure 'data' folder exists
os.makedirs("data", exist_ok=True)

# === Step 3: Save full cleaned book (optional) ===
with open("data/book_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

# === Step 4: Chunk the text ===
chunk_size = 100  # Number of words per chunk
words = cleaned_text.split()
chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# === Step 5: Save the chunks ===
with open("data/book_chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk.strip() + "\n\n")

print(f"✅ Done! Created {len(chunks)} chunks saved to data/book_chunks.txt")
