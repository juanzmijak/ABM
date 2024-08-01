import sqlite3

DATABASE = './test.db'

def verify_tables():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tablas en la base de datos:", tables)

if __name__ == "_main_":
    verify_tables()