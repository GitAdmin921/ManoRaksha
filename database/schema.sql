CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    pseudonymous_id TEXT UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS consent_policies (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    voice_analysis BOOLEAN NOT NULL DEFAULT FALSE,
    typing_analysis BOOLEAN NOT NULL DEFAULT FALSE,
    location_access BOOLEAN NOT NULL DEFAULT FALSE,
    journal_analysis BOOLEAN NOT NULL DEFAULT FALSE,
    passive_monitoring BOOLEAN NOT NULL DEFAULT FALSE,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
