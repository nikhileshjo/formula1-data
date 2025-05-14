CREATE TABLE IF NOT EXISTS session_dim (
    session_id CHAR(32) PRIMARY KEY,
    session_number INT,
    session_type VARCHAR(50)
);
