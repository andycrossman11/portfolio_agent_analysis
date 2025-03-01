CREATE TABLE IF NOT EXISTS position (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ticker TEXT NOT NULL,
    quantity DOUBLE PRECISION NOT NULL,
    purchase_share_price DOUBLE PRECISION NOT NULL,
    purchase_date TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

CREATE TABLE IF NOT EXISTS analysis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    llm_summary TEXT NOT NULL,
    analysis_date TIMESTAMPTZ DEFAULT NOW() NOT NULL
)
