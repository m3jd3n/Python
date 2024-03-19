"""
Napisz program, który analizuje oceny uczniów zapisane w słowniku.
Dla każdego ucznia, program powinien określić kwalifikację na podstawie średniej oceny.

Krok 1: Przygotowanie Danych
        Zdefiniuj słownik zawierający nazwiska uczniów i listy ich ocen.
Krok 2: Analiza Oceny i Przypisanie Kwalifikacji
        Użyj pętli for do iteracji przez słownik i instrukcji warunkowych do przypisania kwalifikacji.
Krok 3: Wyświetlenie Wyników
        Wyświetl kwalifikację każdego ucznia
"""


uczniowie = {
    1: {"imie": "Jan", "nazwisko": "Kowalski", "sredniaOcen": 0, "kwalifikacja": ""},
    2: {"imie": "Jozef", "nazwisko": "Ciesla", "sredniaOcen": 0, "kwalifikacja": ""}
}

przedmioty = {
    1: "j.polski",
    2: "matematyka",
    3: "historia",
    4: "fizyka",
}

oceny = [
    {"uczenId": 1, "przedmiotId": 1, "ocena": 3},
    {"uczenId": 1, "przedmiotId": 2, "ocena": 4},
    {"uczenId": 1, "przedmiotId": 3, "ocena": 4},
    {"uczenId": 1, "przedmiotId": 4, "ocena": 5},
    {"uczenId": 2, "przedmiotId": 1, "ocena": 4},
    {"uczenId": 2, "przedmiotId": 2, "ocena": 5},
    {"uczenId": 2, "przedmiotId": 3, "ocena": 5},
    {"uczenId": 2, "przedmiotId": 4, "ocena": 3}
]


def podaj_int_ocene(uczenId, przedmiotId):
    for ocena in oceny:
        if ocena["uczenId"] == uczenId and ocena["przedmiotId"] == przedmiotId:
            return int(ocena["ocena"])

def wyswietl_oceny_ucznia(uczenId):
    print(f"Oceny ucznia {uczniowie[uczenId]["imie"]} {uczniowie[uczenId]["nazwisko"]}")
    for ocena in oceny:
        if ocena["uczenId"] == uczenId:
            przedmiotNazwa = przedmioty[ocena["przedmiotId"]]
            print(f"{przedmiotNazwa}: {ocena["ocena"]}")
    print(f"Srednia ocen to: {uczniowie[uczenId]["sredniaOcen"]}")
    print(f"Kwalifikacja ucznia to: {uczniowie[uczenId]["kwalifikacja"]}")


def wylicz_srednie_ocen():
    for uczen in uczniowie:
        sumaOcen = 0
        srednia = 0
        for ocena in oceny:
            if ocena["uczenId"] == uczen:
                sumaOcen += ocena["ocena"]
        srednia = int(sumaOcen / len(przedmioty))
        uczniowie[uczen]["sredniaOcen"] = str(srednia)
        if srednia >= 5:
            uczniowie[uczen]["kwalifikacja"] = "Gwiazda klasy - kujonek"
        elif srednia >= 4:
            uczniowie[uczen]["kwalifikacja"] = "Dobry uczen"
        elif srednia >= 3:
            uczniowie[uczen]["kwalifikacja"] = "Minimum oporu"
        elif srednia >= 2:
            uczniowie[uczen]["kwalifikacja"] = "Nerwy ze stali"
        else:
            uczniowie[uczen]["kwalifikacja"] = "Mogloby by lepiej"


def dodaj_ucznia(imie, nazwisko, jpolski, matematyka, historia, fizyka):
    numerNowegoUcznia = len(uczniowie) + 1
    uczniowie[numerNowegoUcznia] = {"imie": imie, "nazwisko": nazwisko, "sredniaOcen": 0, "kwalifikacja": ""}
    oceny.append({"uczenId": numerNowegoUcznia, "przedmiotId": 1, "ocena": jpolski})
    oceny.append({"uczenId": numerNowegoUcznia, "przedmiotId": 2, "ocena": matematyka})
    oceny.append({"uczenId": numerNowegoUcznia, "przedmiotId": 3, "ocena": historia})
    oceny.append({"uczenId": numerNowegoUcznia, "przedmiotId": 4, "ocena": fizyka})




wyswietl_oceny_ucznia(1)
wyswietl_oceny_ucznia(2)
wylicz_srednie_ocen()
wyswietl_oceny_ucznia(1)
wyswietl_oceny_ucznia(2)



dodaj_ucznia("Kasia", "Kowalska", 1 ,2 ,3 ,4)
wyswietl_oceny_ucznia(3)
wylicz_srednie_ocen()
wyswietl_oceny_ucznia(3)
#print(podaj_int_ocene(1, 2))
