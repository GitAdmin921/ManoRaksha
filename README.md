# MANORAKSHA — Mental Health MVP

MANORAKSHA is an early-stage MVP focused on making mental-health support accessible to people who may be distressed, overwhelmed, or unable to navigate a conventional application.

> **Important:** This repository is an MVP/prototype architecture, not a medical device or replacement for qualified mental-health professionals or emergency services.

## 1. MVP Goal

The first phase is **Research Planning**:

- Understand the user's problem and real-world needs.
- Study atrocities/trauma-related contexts and their impact on communication and help-seeking.
- Design communication that can work when a person cannot comfortably operate a normal app UI.
- Explore **AI voice/video communication** as an accessibility-first interface.
- Keep a human/professional support path available.
- Build privacy, consent, safety, and escalation into the architecture from the beginning.

## 2. Product Principle

**The user should not have to fight the interface when their mind is already overloaded.**

The MVP therefore separates:

1. **Conversation layer** — voice/video/text interaction.
2. **AI assistance layer** — safe conversational support and routing.
3. **Safety layer** — crisis detection, escalation and human handoff.
4. **Data layer** — minimum necessary storage with privacy controls.
5. **Research layer** — anonymized/consented data for learning and validation.

## 3. Repository Structure

```text
MANORAKSHA/
├── frontend/              # Web/mobile-friendly client
├── backend/               # API + WebSocket service
├── ai/                    # AI orchestration and safety logic
├── database/              # DB schema/migrations
├── docs/                  # Research, architecture and safety documents
├── edge/                  # Optional future low-connectivity/edge components
├── infra/                 # Deployment configuration
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```

## 4. Technology Direction

### Frontend
- React
- TypeScript
- Vite
- Responsive/mobile-first UI
- WebRTC/WebSocket integration planned

### Backend
- Python
- FastAPI
- WebSocket support
- REST APIs

### Data
- PostgreSQL
- Redis (optional for sessions/queues)
- Encryption and access control required before real sensitive data is used

### AI
AI components should be isolated behind a service interface so the model/provider can be changed without rewriting the application.

## 5. High-Level Flow

```text
User
  │
  ├── Voice ─────┐
  ├── Video ─────┼──> Frontend
  └── Text ──────┘       │
                         ▼
                    Backend API
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        AI Orchestrator        Safety Layer
              │                     │
              └──────────┬──────────┘
                         ▼
                  Human/Professional
                    Support Path
                         │
                         ▼
                    Data Layer
```

## 6. Safety Requirements

This project concerns a sensitive domain. Before production use:

- Do not present the AI as a therapist unless appropriately validated and legally approved.
- Provide clear emergency/crisis guidance.
- Define human escalation rules.
- Obtain informed consent where required.
- Minimize collection and retention of sensitive data.
- Encrypt data in transit and at rest.
- Keep audit logs for safety-critical events without unnecessarily storing conversation content.
- Perform security, privacy, clinical/safety and legal review.

## 7. Local Development

### Prerequisites

Install:

- Git
- Python 3.11+
- Node.js 20+
- Docker Desktop (optional but recommended)

### Clone

```bash
git clone https://github.com/MANORAKSHA/demo-repository.git
cd demo-repository
```

### Backend

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Health check:

```text
GET /health
```

### Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open the Vite URL shown in the terminal.

## 8. Environment Variables

Copy:

```bash
cp .env.example .env
```

Never commit `.env`.

Example:

```env
APP_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/manoraksha
REDIS_URL=redis://localhost:6379
AI_PROVIDER=
AI_API_KEY=
```

## 9. Docker

From the repository root:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

## 10. Git Workflow

```bash
git status
git add .
git commit -m "Initial MANORAKSHA MVP structure"
git push origin main
```

## 11. Hosting Roadmap

### Recommended MVP deployment

**Frontend:** Vercel  
**Backend:** Render/Railway/Fly.io or another HTTPS-capable platform  
**Database:** Managed PostgreSQL  
**Redis:** Managed Redis if required

Do not put secret API keys in the frontend.

### Frontend deployment

1. Push repository to GitHub.
2. Open Vercel.
3. Import the GitHub repository.
4. Set the frontend root directory to `frontend`.
5. Build command: `npm run build`.
6. Output directory: `dist`.
7. Add only public frontend environment variables.
8. Deploy.
9. Configure the backend URL in the frontend.

### Backend deployment

1. Create a backend service on the chosen host.
2. Set root directory to `backend`.
3. Install command:

```bash
pip install -r requirements.txt
```

4. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

5. Add backend secrets through the host's environment-variable settings.
6. Add a managed PostgreSQL database.
7. Configure CORS for the frontend domain.
8. Enable HTTPS.
9. Test `/health`.

### Database

Never expose PostgreSQL directly to the public internet.

Use a managed private/secured database and:

- strong credentials
- TLS
- backups
- least-privilege database users
- retention policy

## 12. GitHub Secrets / Production Secrets

Never commit:

```text
.env
AI_API_KEY
DATABASE_PASSWORD
JWT_SECRET
PRIVATE_KEYS
```

Use the hosting provider's secret/environment-variable system.

## 13. Suggested Development Phases

### Phase 1 — Research
- Problem definition
- User interviews/research
- Atrocity/trauma context study
- Accessibility requirements
- Safety requirements
- Consent/privacy requirements

### Phase 2 — UX Prototype
- Voice-first flow
- Video communication flow
- Minimal UI
- Human handoff
- Emergency/safety states

### Phase 3 — Technical MVP
- Frontend
- Backend
- Authentication
- WebSocket communication
- AI service abstraction
- Safety service

### Phase 4 — Validation
- Security testing
- Usability testing
- Safety review
- Human/professional review
- Performance testing

### Phase 5 — Controlled Pilot
Only after appropriate safety, privacy, legal and professional review.

## 14. Current Status

This repository is an **architecture and MVP foundation**. It should not be treated as production-ready clinical software.

The handwritten mind map supplied for the MANORAKSHA project is the source of truth for product direction; implementation should be updated to match validated research decisions rather than blindly following an earlier generic full-stack template.
