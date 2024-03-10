class NieprawidlowaWartosc(Exception):
    pass

def dzielenie(a,b):

    try:
        a,b = int(a), int(b)
        if b == 0:
            raise NieprawidlowaWartosc("Nie mozna dzielic przez 0!")

    except ValueError:
        return "Nieprawidlowe wartosci!"

    except NieprawidlowaWartosc as e:
        return str(e)
    else:
        return a / b

d = ("")
while d.lower() != "x":
    a = input("Podaj pierwsza liczbe: ")
    b = input("Podaj druga liczbe: ")
    print(dzielenie(a,b))
    d = input("Wcisnij x aby zakonczyc lub ENTER klawisz aby kontynuowac: ")
    print("\n")
