CREATE TABLE IF NOT EXISTS position (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ticker TEXT NOT NULL,
    quantity DOUBLE PRECISION NOT NULL,
    total_purchase_price DOUBLE PRECISION NOT NULL,
    purchase_date TIMESTAMPTZ DEFAULT NOW() NOT NULL
);
