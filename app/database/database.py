import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def create_tables():
    """Создание таблиц для пользователей и результатов тестов."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
            score INTEGER NOT NULL,
            correct_answers TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
