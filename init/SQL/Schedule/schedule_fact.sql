CREATE TABLE schedule_fact (
    schedule_id INT PRIMARY KEY,
    round_number INT,
    location_id INT,
    event_id INT,
    session_id INT,
    date_id INT,
    
    FOREIGN KEY (location_id) REFERENCES location_dim(location_id),
    FOREIGN KEY (event_id) REFERENCES event_dim(event_id),
    FOREIGN KEY (session_id) REFERENCES session_dim(session_id),
    FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
);
