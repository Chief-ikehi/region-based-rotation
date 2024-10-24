CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    region VARCHAR(50) NOT NULL,
    question_text TEXT NOT NULL
);

CREATE TABLE cycle_config (
    id SERIAL PRIMARY KEY,
    region VARCHAR(50) NOT NULL,
    cycle_duration INT NOT NULL,
    start_time TIMESTAMP NOT NULL
);

CREATE TABLE current_cycle (
    id SERIAL PRIMARY KEY,
    region VARCHAR(50) NOT NULL,
    current_cycle INT NOT NULL,
    last_update TIMESTAMP
);
