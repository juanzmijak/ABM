import os
import sqlite3

DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test.db'))

def create_tables():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                edad INTEGER NOT NULL
            )
        ''')

if __name__ == "__main__":
    create_tables()