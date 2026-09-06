import sqlite3
from pathlib import Path

DB_path = Path(__file__).parent / "SQLiteDataBase.db"

def get_connection():
    return sqlite3.connect(DB_path)
