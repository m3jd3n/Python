import time

def zmierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        czas_rozpoczecia = time.time()
        wynik = funkcja(*args)
        czas_zakonczenia = time.time()
        czas_wykonania = czas_zakonczenia - czas_rozpoczecia
        return wynik, czas_wykonania
    return wrapper

def ciag(ile_liczb):
    liczba = 0
    licznik = 0
    while licznik <= ile_liczb:
        liczba = liczba + licznik;
        licznik += 1
    return liczba

dzialanie = zmierz_czas(ciag)
print(dzialanie(5))




