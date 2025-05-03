import logging
from functools import reduce
logging.basicConfig(level=logging.INFO)
def dodaj_wszystkie(lista_liczb):
    return sum(lista_liczb)
def odejmij_wszystkie(lista_liczb):
    return reduce(lambda x, y: x - y, lista_liczb)
def mnoz_wszystkie(lista_liczb):
    wynik = 1
    for liczba in lista_liczb:
        wynik *= liczba
    return wynik
def dziel_wszystkie(lista_liczb):
    try:
        return reduce(lambda x, y: x / y, lista_liczb)
    except ZeroDivisionError:
        raise ValueError("Nie można dzielić przez zero!")
def main():
    dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    liczby = input("Podaj liczby, oddzielone spacją: ").split()
    liczby = [float(liczba) for liczba in liczby]
    
    if dzialanie == '1':
        logging.info(f"Dodaję {', '.join(map(str, liczby))}")
        wynik = dodaj_wszystkie(liczby)
    elif dzialanie == '2':
        logging.info(f"Odejmuję {', '.join(map(str, liczby))}")
        wynik = odejmij_wszystkie(liczby)
    elif dzialanie == '3':
        logging.info(f"Mnożę {', '.join(map(str, liczby))}")
        wynik = mnoz_wszystkie(liczby)
    elif dzialanie == '4':
        logging.info(f"Dzielę {', '.join(map(str, liczby))}")
        try:
            wynik = dziel_wszystkie(liczby)
        except ValueError as e:
            logging.error(e)
            return
    else:
        logging.error("Nieznane działanie!")
        return

    print(f"Wynik to {wynik}")

if __name__ == "__main__":
    main()

    
