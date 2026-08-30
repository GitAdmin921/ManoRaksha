import React, { useState } from "react";
import { createRoot } from "react-dom/client";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "https://manoraksha-1.onrender.com";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function startConversation() {
    const text = message.trim();
    if (!text) {
      setError("Please write a message first.");
      return;
    }

    setLoading(true);
    setError("");
    setReply("");

    try {
      const response = await fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(data.detail || `Server error (${response.status})`);
      }

      setReply(data.reply || "I received your message, but no reply was returned.");
    } catch (err) {
      console.error(err);
      setError(`Could not connect to MANORAKSHA AI: ${err.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main style={{ maxWidth: 720, margin: "0 auto", padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <h1>MANORAKSHA</h1>
      <p>Mental-health support MVP — accessibility-first and safety-first.</p>
      <p>This is an early prototype and is not a replacement for professional or emergency care.</p>

      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Tell me what is on your mind..."
        rows={5}
        style={{ width: "100%", boxSizing: "border-box", padding: 12, borderRadius: 10 }}
      />

      <button
        type="button"
        onClick={startConversation}
        disabled={loading}
        style={{ marginTop: 12, padding: "12px 18px", borderRadius: 10, cursor: loading ? "wait" : "pointer" }}
      >
        {loading ? "Connecting..." : "Start a conversation"}
      </button>

      {error && <p role="alert" style={{ marginTop: 16 }}>{error}</p>}
      {reply && (
        <section style={{ marginTop: 20, padding: 16, border: "1px solid #ddd", borderRadius: 12 }}>
          <strong>MANORAKSHA AI</strong>
          <p style={{ whiteSpace: "pre-wrap" }}>{reply}</p>
        </section>
      )}
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
