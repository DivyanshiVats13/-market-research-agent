import { useState } from "react";
import ReactMarkdown from "react-markdown";

function App() {
  const [topic, setTopic] = useState("");
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const handleResearch = async () => {
    if (!topic) return;
    setLoading(true);
    setReport("");
    try {
      const res = await fetch("https://market-research-agent-ijky.onrender.com/research", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic }),
      });
      const data = await res.json();
      setReport(data.report);
    } catch (err) {
      setReport("Error: Could not connect to backend.");
    }
    setLoading(false);
  };

  return (
    <div style={{ minHeight: "100vh", backgroundColor: "#000", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: "'Segoe UI', sans-serif", padding: "40px 20px" }}>
      
      <h1 style={{ color: "#fff", fontSize: "32px", margin: "0 0 8px" }}>🔍 AI Market Research Agent</h1>
      <p style={{ color: "#666", margin: "0 0 40px", fontSize: "15px" }}>Powered by CrewAI · Groq · Tavily</p>

      <div style={{ width: "100%", maxWidth: "700px" }}>
        <div style={{ display: "flex", gap: "10px", marginBottom: "24px" }}>
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleResearch()}
            placeholder="e.g. AI tools for HR teams"
            style={{ flex: 1, padding: "14px 18px", fontSize: "15px", borderRadius: "8px", border: "1px solid #333", backgroundColor: "#111", color: "#fff", outline: "none" }}
          />
          <button
            onClick={handleResearch}
            disabled={loading}
            style={{ padding: "14px 28px", backgroundColor: loading ? "#333" : "#fff", color: loading ? "#888" : "#000", border: "none", borderRadius: "8px", fontSize: "15px", cursor: loading ? "not-allowed" : "pointer", fontWeight: "700" }}
          >
            {loading ? "Working..." : "Research"}
          </button>
        </div>

        {loading && (
          <div style={{ textAlign: "center", padding: "60px", color: "#666" }}>
            <div style={{ fontSize: "40px", marginBottom: "16px" }}>🤖</div>
            <p style={{ color: "#aaa", fontSize: "16px" }}>3 AI agents are working on your report...</p>
            <p style={{ color: "#555", fontSize: "13px" }}>Researcher → Analyst → Report Writer · ~60 seconds</p>
          </div>
        )}

        {report && (
          <div style={{ backgroundColor: "#111", border: "1px solid #222", borderRadius: "12px", padding: "32px", color: "#ddd", lineHeight: "1.8" }}>
            <ReactMarkdown>{report}</ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;