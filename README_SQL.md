# Projekt SQL

## Opis
Ten projekt zawiera przykładowe skrypty SQL oraz kod Pythona do tworzenia i zarządzania bazą danych SQLite.  
Projekt ma na celu naukę podstaw SQL i praktyczne zastosowanie baz danych.

## Funkcjonalności
- Tworzenie bazy danych SQLite
- Tworzenie tabel (`projects`, `tasks`, `students` itp.)
- Wstawianie danych do tabel
- Odczyt danych z tabel
- Przykładowe zapytania SELECT

## Struktura projektu
- `01_create_db.py` – skrypt tworzący bazę danych i tabele  
- `02_read_data.py` – skrypt odczytujący dane z bazy i wyświetlający je  
- `database.db` – plik z bazą danych SQLite (generowany automatycznie)

## Jak uruchomić
1. Uruchom `01_create_db.py`, aby stworzyć bazę danych i tabele.  
2. Uruchom `02_read_data.py`, aby zobaczyć zawartość tabel.

## Wymagania
- Python 3.x  
- Biblioteka `sqlite3` (wbudowana w Pythona)

## Autor
Adam Salamonowicz  
[https://github.com/SAdam15](https://github.com/SAdam15)