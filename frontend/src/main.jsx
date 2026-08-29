import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return (
    <main style={{maxWidth: 720, margin: "0 auto", padding: 24, fontFamily: "system-ui"}}>
      <h1>MANORAKSHA</h1>
      <p>Mental-health support MVP — voice-first, safety-first.</p>
      <p>This is an early prototype. It is not a replacement for professional or emergency care.</p>
      <button>Start a conversation</button>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
