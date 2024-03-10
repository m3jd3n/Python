class Pojazd:
    def __init__(self, marka=None, model=None, rok=None, liczba_kol=4):
        self.rok = rok
        self.marka = marka
        self.model = model
        self.liczba_kol = liczba_kol

    def wyswietl_info(self):
        return f"Samochód: {self.marka} {self.model} {self.rok} {self.liczba_kol}"


moj_pojazd = Pojazd("Toyota", "Corolla", 2020)
moj_pojazd_1 = Pojazd()
moj_pojazd_2 = Pojazd(2020)
moj_pojazd_3 = Pojazd(rok = 2020)

print(moj_pojazd.wyswietl_info())
print(moj_pojazd_1.wyswietl_info())
print(moj_pojazd_2.wyswietl_info())
print(moj_pojazd_3.wyswietl_info())

help(Pojazd)