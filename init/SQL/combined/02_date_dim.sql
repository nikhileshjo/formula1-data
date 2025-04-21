CREATE TABLE IF NOT EXISTS date_dim (
    date_id INT PRIMARY KEY,
    full_timestamp TIMESTAMP,
    local_timestamp TIMESTAMP,
    day_of_week VARCHAR(20),
    month_name VARCHAR(20),
    year INT,
    quarter INT CHECK (quarter >= 1 AND quarter <= 4),
    is_night_race BOOLEAN
);