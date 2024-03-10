class NieprawidlowaWartosc(Exception):
    pass


def dzielenie(x, y):

    try:
        x, y = int(x), int(y)
        if y == 0:
            raise NieprawidlowaWartosc("Nie mozna dzielic przez 0!")

    except ValueError:
        return "Nieprawidlowe wartosci!"

    except NieprawidlowaWartosc as e:
        return str(e)
    else:
        return x / y


d = ""


while True:
    a = input("Podaj pierwsza liczbe: ")
    b = input("Podaj druga liczbe: ")
    print(dzielenie(a, b))
    d = input("Wcisnij x aby zakonczyc lub ENTER klawisz aby kontynuowac: ")
    if d == "x":
        break
    print("\n")
