CREATE TABLE IF NOT EXISTS schedule_fact (
    schedule_id INT PRIMARY KEY,
    location_id CHAR(32),
    event_id CHAR(32),
    session_id CHAR(32),
    date_id INT,
    
    FOREIGN KEY (location_id) REFERENCES location_dim(location_id),
    FOREIGN KEY (event_id) REFERENCES event_dim(event_id),
    FOREIGN KEY (session_id) REFERENCES session_dim(session_id),
    FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
);
