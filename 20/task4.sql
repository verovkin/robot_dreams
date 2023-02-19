CREATE TABLE IF NOT EXISTS usr3(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    UNIQUE (first_name, last_name)
)