# 🔍 AI Market Research Agent

🔗 **[Live Demo](https://market-research-agent-snowy.vercel.app)**

An AI research agent that takes any topic or question and returns a clear, well-grounded answer — built with **LangGraph** to actually reason about whether its research is good enough before answering, rather than following a fixed, one-shot pipeline.

Instead of relying purely on an LLM's internal knowledge (which can be outdated or hallucinated), every response is grounded in **live web search results**, evaluated for sufficiency, and only then synthesized into an answer.

---

## 🧠 How It Works

This is built as a **LangGraph state graph** with three nodes and a conditional decision point — not just a linear chain of function calls.

```
        ┌────────┐
        │ search │◄────────────┐
        └───┬────┘              │
            │                   │ insufficient
            ▼                   │ (max 1 retry)
        ┌─────────┐             │
        │ analyze │─────────────┘
        └───┬─────┘
            │ sufficient
            ▼
        ┌────────┐
        │ report │
        └───┬────┘
            │
            ▼
           END
```

1. **Search node** — Sends the topic to the [Tavily](https://tavily.com) Search API and retrieves relevant, up-to-date web results.

2. **Analyze node** — This is the real decision-making step. An LLM call ([Groq](https://groq.com), Llama 3.3 70B) reads the search results and judges whether they actually contain enough specific, relevant information to answer the topic well. It outputs a sufficiency judgment and, if the results are weak, suggests a refined search query.

3. **Conditional edge** — If the analyst judges the research insufficient, the graph routes back to the search node with the refined query (capped at 1 retry to avoid infinite loops). If sufficient, it proceeds to the report node.

4. **Report node** — Takes the (now-validated) research and synthesizes it into a direct, conversational answer — not a rigid report format.

This retry loop is what makes the system genuinely agentic rather than a fixed sequence: the graph's path through the nodes depends on the LLM's own judgment of the intermediate output, not a hardcoded flow.

---

## ⚙️ Tech Stack

**Backend**
- **FastAPI** (Python) — API server exposing a single `/research` endpoint
- **LangGraph** — orchestrates the search → analyze → (conditional retry) → report flow as a stateful graph
- **Tavily API** — real-time web search
- **Groq API** — fast LLM inference (Llama 3.3 70B), used for both the analysis judgment and final report generation
- **Deployment**: Render

**Frontend**
- **React** (Create React App)
- **react-markdown** — renders the AI's markdown response
- **Deployment**: Vercel

---

## ✨ Features

- Single-input interface — type any topic or question, get a researched answer
- Real-time web grounding, not just LLM memory
- A genuine agentic decision point — the system evaluates its own research and can retry with a better query before answering
- Fast responses thanks to Groq's inference speed
- Fully deployed, live, and usable end-to-end

---

## 🗂️ Project Structure

```
market-research-agent/
├── backend/
│   ├── main.py              # FastAPI app — /research endpoint
│   ├── graph.py              # LangGraph pipeline: nodes, state, conditional edges
│   ├── requirements.txt
│   └── .env                  # API keys (not committed)
│
└── frontend/
    ├── src/
    │   ├── App.js             # Main UI — input box, fetch call, markdown rendering
    │   └── App.css
    ├── public/
    └── package.json
```

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
```
TAVILY_API_KEY=your_tavily_key_here
GROQ_API_KEY=your_groq_key_here
```
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

- Add source citations inline in the generated report
- Cache recent queries to reduce redundant API calls
- Add multi-turn follow-up questions instead of single-shot queries
- Add a dedicated "writer" node separate from the analyst, so report tone/structure can be tuned independently of the sufficiency judgment
- Increase max retries with smarter query refinement for genuinely obscure topics

---

## 👤 Author

Built by **Divyanshi Vats**
[GitHub](https://github.com/DivyanshiVats13)