# 💡 LMIS Bot – Last Minute Interview Saver

> *“Because when you're 12 hours from an AIML interview, coffee isn’t enough — you need a chatbot who knows your pain.”*

LMIS Bot is my personal AI-powered chatbot to help me **revise AIML interview topics** in the crunch hour. It's not just a project — it's my 2 AM accountability partner, my digital study buddy, and possibly the reason I’ll sleep better before interviews.

---

## 🚀 Why I Built This

Every AIML student knows this moment:
> The interview is tomorrow. You’ve read everything, but your brain is stuck on ‘What’s overfitting?’ — again.

I needed something quick, smart, and interactive to quiz me without the pressure of people watching. So, I built **LMIS Bot** — a chatbot powered by RNN (LSTM), fine-tuned on AIML questions I personally curated.

---

## 🧠 How It Works (In My Words)

- You ask a technical question from AIML, like:
  - “What is overfitting?”
  - “Explain bias-variance tradeoff.”
  - “What’s the difference between bagging and boosting?”

- It responds just like a mentor would (without judgment).

- You get smarter, faster, and more confident — one chat at a time.

---

## ⚙️ Tech Stack

| Part          | Tools Used                                    |
| ------------- | --------------------------------------------- |
| Retrieval     | TF-IDF Vectorizer (Scikit-learn)              |
| Backend       | Flask (Python)                                |
| Frontend      | HTML, CSS, React.js                           |
| Data Format   | Text chunks (from `.txt`) + similarity search |
| Communication | REST API + JSON                               |
| Container     | Docker                                        |
| Deployment    | Azure Web App for Containers + Static Web App |


---

## 📆 My 7-Day Agile Sprint Plan (Solo Scrum)


| Day | Task | Status | Completion Date |
|-----|------|--------|-----------------|
| Day 1 | 📖 Data Preprocessing – Clean & Chunk Book | Completed | 31/07/2025 |
| Day 2 | 🔍 Build TF-IDF Retriever – Search over chunks | Completed | 01/08/2025 |
| Day 3 | 🧠 Create Flask API – Serve chatbot responses | Completed  | 04/08/2025 |
| Day 4 | 💬 Build React Frontend – Chat UI integration |  |  |
| Day 5 | ✨ Improve with Sentence Embeddings (optional) |  |  |
| Day 6 | 🐳 Dockerize and Deploy to Azure |  |  |
| Day 7 | ✅ Testing, UI polish & Documentation |  |  |