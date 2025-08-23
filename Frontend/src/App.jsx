import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error("Error fetching answer:", error);
      setAnswer("⚠️ Error: Could not connect to backend.");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Y4D Chatbot</h1>

      <textarea
        placeholder="Ask me anything about Y4D..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows={4}
        style={{ width: "100%", marginBottom: "1rem" }}
      />

      <br />
      <button onClick={handleAsk}>Ask</button>

      {answer && (
        <div style={{ marginTop: "1rem", padding: "1rem", border: "1px solid #ccc" }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
