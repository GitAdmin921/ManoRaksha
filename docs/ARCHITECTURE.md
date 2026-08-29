# MANORAKSHA Architecture

## Core layers

```text
User
 ↓
Voice / Video / Text Interface
 ↓
Session + Communication Service
 ↓
AI Orchestrator
 ├── Conversation
 ├── Context
 └── Safety
 ↓
Human / Professional Handoff
 ↓
Secure Data Layer
```

The architecture is intentionally modular. AI, communication, storage and safety components should be replaceable independently.

## Non-functional priorities

1. Safety
2. Privacy
3. Accessibility
4. Reliability
5. Usability
6. Cost/performance
