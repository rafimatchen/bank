DROP TABLE IF EXISTS code;

CREATE TABLE security_code (
    id PRIMARY KEY,
    code TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);