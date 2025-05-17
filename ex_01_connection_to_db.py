import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Nawiązuje połączenie z bazą SQLite (plik)"""
    try:
        conn = sqlite3.connect(db_file)
        print(f"Połączono z {db_file}")
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn):
    """Tworzy tabelę students jeśli nie istnieje"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            grade REAL
        );
        """)
        print("Tabela 'students' została utworzona (jeśli nie istniała).")
    except Error as e:
        print(e)

def insert_student(conn, name, surname, grade):
    """Dodaje nowego studenta do tabeli"""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, surname, grade) VALUES (?, ?, ?)", (name, surname, grade))
        conn.commit()
        print(f"Dodano studenta: {name} {surname}, ocena: {grade}")
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection("database.db")
    if conn:
        create_table(conn)
        insert_student(conn, "Adam", "Salamonowicz", 5.0)
        insert_student(conn, "Anna", "Nowak", 4.5)
        conn.close()