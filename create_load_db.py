import sqlite3
import csv

def drop_tables(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS measure")
    cursor.execute("DROP TABLE IF EXISTS stations")
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stations (
            station TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL,
            elevation REAL,
            name TEXT,
            country TEXT,
            state TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measure (
            station TEXT,
            date TEXT,
            precip REAL,
            tobs INTEGER,
            FOREIGN KEY(station) REFERENCES stations(station)
        )
    ''')
    conn.commit()

def load_stations(conn, filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['station'], float(row['latitude']), float(row['longitude']),
                 float(row['elevation']), row['name'], row['country'], row['state'])
                for row in reader]
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR REPLACE INTO stations (station, latitude, longitude, elevation, name, country, state)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()

def load_measure(conn, filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            precip = float(row['precip']) if row['precip'] else None
            tobs = int(row['tobs']) if row['tobs'] else None
            data.append((row['station'], row['date'], precip, tobs))
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO measure (station, date, precip, tobs)
        VALUES (?, ?, ?, ?)
    ''', data)
    conn.commit()

def main():
    db_name = 'public_transport.db'
    stations_file = r'C:\Users\abero\Downloads\clean_stations.csv'  # wpisz tutaj swoją ścieżkę
    measure_file = r'C:\Users\abero\Downloads\clean_measure.csv'    # wpisz tutaj swoją ścieżkę

    conn = sqlite3.connect(db_name)

    drop_tables(conn)
    create_tables(conn)
    print("Tworzenie tabel zakończone.")

    load_stations(conn, stations_file)
    print("Dane z stations załadowane.")

    load_measure(conn, measure_file)
    print("Dane z measure załadowane.")

    print("\nPrzykładowe dane z tabeli stations:")
    for row in conn.execute("SELECT * FROM stations LIMIT 5"):
        print(row)

    print("\nPrzykładowe dane z tabeli measure:")
    for row in conn.execute("SELECT * FROM measure LIMIT 5"):
        print(row)

    conn.close()
    print("\nZakończono.")

if __name__ == '__main__':
    main()