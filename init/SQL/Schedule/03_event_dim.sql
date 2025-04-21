CREATE TABLE IF NOT EXISTS event_dim (
    event_id INT PRIMARY KEY,
    official_event_name VARCHAR(300),
    event_name VARCHAR(100),
    event_type varchar(100)
);
