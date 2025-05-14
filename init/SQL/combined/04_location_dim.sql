CREATE TABLE IF NOT EXISTS location_dim (
    location_id CHAR(32) PRIMARY KEY,
    location_name VARCHAR(100),
    country_name VARCHAR(100)
);
