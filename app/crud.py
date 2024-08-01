import os
import sqlite3
from contextlib import closing
from .schemas import UserCreate, User

DATABASE = os.path.abspath(os.path.join(os.path.dirname(_file_), '../test.db'))

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(user: UserCreate):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO users (nombre, apellido, direccion, telefono, edad)
            VALUES (?, ?, ?, ?, ?)
        ''', (user.nombre, user.apellido, user.direccion, user.telefono, user.edad))
        db.commit()
        return cursor.lastrowid

def get_user(user_id: int):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return User(id=row[0], nombre=row[1], apellido=row[2], direccion=row[3], telefono=row[4], edad=row[5])

def get_user_by_name(nombre: str):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE nombre LIKE ?', (f'%{nombre}%',))
        rows = cursor.fetchall()
        return [User(id=row[0], nombre=row[1], apellido=row[2], direccion=row[3], telefono=row[4], edad=row[5]) for row in rows]

def update_user(user_id: int, user: UserCreate):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('''
            UPDATE users SET nombre = ?, apellido = ?, direccion = ?, telefono = ?, edad = ?
            WHERE id = ?
        ''', (user.nombre, user.apellido, user.direccion, user.telefono, user.edad, user_id))
        db.commit()
        return get_user(user_id)

def delete_user(user_id: int):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        db.commit()
        return True