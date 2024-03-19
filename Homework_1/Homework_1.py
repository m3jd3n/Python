"""Opis Zadania:
Stwórz grę, w której użytkownik musi odgadnąć losowo wygenerowany numer. Użytkownik ma ograniczoną
liczbę prób. Po każdej próbie, program powinien informować, czy podana liczba jest za duża, za mała, czy
prawidłowa. Jeśli użytkownik nie odgadnie liczby w wyznaczonej liczbie prób, gra kończy się porażką.
Krok 1: Importowanie Modułu i Inicjalizacja Zmiennych
Importuj moduł random do wygenerowania losowego numeru i zdefiniuj zmienne.
Krok 2: Pętla while dla Gry
Użyj pętli while do przetwarzania prób użytkownika.
Krok 3: Sprawdzenie Warunku Zakończenia Gry
Jeśli użytkownik nie zgadnie liczby w wyznaczonej liczbie prób, gra kończy się"""


import random
dolZakresuLiczb = 1
goraZakresuLiczb = 20
iloscProb = 5

zgadywanaLiczba = random.randint(dolZakresuLiczb, goraZakresuLiczb)

pozostaloProb = iloscProb

while pozostaloProb > 0:
    probaZgadniecia = int(input(f"Zgadnij liczbę między {dolZakresuLiczb} a {goraZakresuLiczb} "))

    if probaZgadniecia < zgadywanaLiczba:
        print("Za mała liczba.")
    elif probaZgadniecia > zgadywanaLiczba:
        print("Za duża liczba.")
    else:
        print("Zgadłeś liczbe!!!")
        break

    pozostaloProb -= 1
    print(f"Pozostało prób: {pozostaloProb}")

else:
    print(f"Nie udalo sie. Zgadywana liczna to: {zgadywanaLiczba}.")