# 🔍 AI Market Research Agent

🔗 **[Live Demo](https://market-research-agent-snowy.vercel.app)**

An AI-powered market research tool that takes any topic or question and returns a clear, well-grounded answer in seconds. Instead of relying purely on an LLM's internal knowledge (which can be outdated or hallucinated), this project grounds every response in **live web search results**, then uses an LLM to synthesize those results into a direct, readable answer.

Built as a full-stack project to explore how to combine real-time information retrieval with fast LLM inference in a production-style deployment (not just a notebook demo).

---

## 🧠 How It Works

The pipeline behind every query has three steps:

1. **Search** — When a user submits a topic, the backend sends the query to the [Tavily](https://tavily.com) Search API, which returns a set of relevant, up-to-date web results (titles, URLs, and content snippets).

2. **Synthesize** — The raw search results are compiled into context and passed to an LLM via the [Groq](https://groq.com) API (running **Llama 3.3 70B**). The model is prompted to read through the search context and produce a direct, conversational answer grounded in that information — not a generic AI response.

3. **Respond** — The synthesized answer is sent back to the React frontend and rendered as formatted markdown, so links, bold text, and lists display cleanly.

This approach means the tool can answer questions about very recent events, tools, or trends that a base LLM alone wouldn't know about, since the answer is always backed by fresh search results rather than static training data.

---

## ⚙️ Tech Stack

**Backend**
- **FastAPI** (Python) — lightweight API server exposing a single `/research` endpoint
- **Tavily API** — real-time web search
- **Groq API** — fast LLM inference (Llama 3.3 70B)
- **Deployment**: Render

**Frontend**
- **React** (Create React App)
- **react-markdown** — renders the AI's markdown response as formatted HTML
- **Deployment**: Vercel

---

## ✨ Features

- Single-input interface — type any topic or question, get a researched answer
- Real-time web grounding, not just LLM memory — results reflect current information
- Fast responses thanks to Groq's inference speed
- Clean, minimal dark-themed UI focused on readability
- Fully deployed, live, and usable end-to-end (not just a local demo)

---

## 🗂️ Project Structure

market-research-agent/
├── backend/
│   ├── main.py              # FastAPI app — /research endpoint, Tavily + Groq calls
│   ├── agents/               # Modular logic for research/analysis steps
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # API keys (not committed)
│
└── frontend/
├── src/
│   ├── App.js             # Main UI — input box, fetch call, markdown rendering
│   └── App.css
├── public/
└── package.json

---

## 🚀 Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/DivyanshiVats13/-market-research-agent.git
cd market-research-agent
```

**2. Backend setup**
```bash
cd backend
pip install -r requirements.txt
```
Create a `.env` file inside `backend/` with:

TAVILY_API_KEY=your_tavily_key_here
GROQ_API_KEY=your_groq_key_here

Then run:
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

**3. Frontend setup**
```bash
cd frontend
npm install
npm start
```
The app will be available at `http://localhost:3000`.

---

## 🔮 Possible Future Improvements

- Add source citations inline in the generated report (currently sources are used but not explicitly linked in output)
- Cache recent queries to reduce redundant API calls
- Add multi-turn follow-up questions instead of single-shot queries
- Expand into a true multi-agent pipeline (separate research, analysis, and writing agents) for more structured, longer-form reports

---

## 👤 Author

Built by **Divyanshi Vats**
[GitHub](https://github.com/DivyanshiVats13)