import sqlite3
from pathlib import Path

DB_PATH = Path("shortner.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db():
    with get_connection() as conn:
        conn.executescript(""" 
                           CREATE TABLE IF NOT EXISTS links(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               original_url TEXT NOT NULL,
                               short_code TEXT NOT NULL UNIQUE,
                               created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                               expires_at DATETIME DEFAULT NULL
                               );
                               CREATE INDEX IF NOT EXISTS idx_links_short_code ON links(short_code);
                               """)