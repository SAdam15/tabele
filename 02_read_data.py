import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Nawiązuje połączenie z bazą danych SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Połączono z bazą danych:", db_file)
    except Error as e:
        print("Błąd połączenia:", e)
    return conn

def select_all_projects(conn):
    """Pobiera i wyświetla wszystkie projekty."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects")
        rows = cur.fetchall()

        print("=== Projekty ===")
        for row in rows:
            print(row)
    except Error as e:
        print("Błąd przy odczycie projektów:", e)

def select_all_tasks(conn):
    """Pobiera i wyświetla wszystkie zadania."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()

        print("=== Zadania ===")
        for row in rows:
            print(row)
    except Error as e:
        print("Błąd przy odczycie zadań:", e)

def main():
    database = "database.db"
    conn = create_connection(database)

    if conn is not None:
        select_all_projects(conn)
        select_all_tasks(conn)
        conn.close()
    else:
        print("Brak połączenia z bazą danych.")

if __name__ == "__main__":
    main()
