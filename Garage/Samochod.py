class Garage:


    def __init__(self, adres="Unknown", pojemnosc=0):
        self.adres = adres
        self.pojemnosc = pojemnosc
        self.liczba_samochodow = 0
        self.lista = []

    def __str__(self):
        opis = "Adres: " + self.adres
        opis += "\nPojemność: " + str(self.pojemnosc)
        opis += "\nLiczba samochodów: " + str(self.liczba_samochodow)
        for i in self.lista:
            opis += "\n"
            opis += str(i)
        return opis

    def dodaj_samochod(self, samochod):
        if self.liczba_samochodow < self._pojemnosc:
            self.lista.append(samochod)
            self.liczba_samochodow += 1
        else:
            print("Brak miejsca w garażu")

    def usun_samochod(self, numer_rejestracyjny):
        for x in self.lista:
            if x.numer_rejestracyjny == numer_rejestracyjny:
                self.lista.remove(x)
                self.liczba_samochodow -= 1

    @property
    def adres(self):
        return self._adres

    @adres.setter
    def adres(self, nowy_adres):
        if nowy_adres == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_adres, (float, int)):
            print("Adres nie moze być liczbą")
        else:
            self._adres = nowy_adres

    @property
    def pojemnosc(self):
        return self._pojemnosc

    @pojemnosc.setter
    def pojemnosc(self, nowa_pojemnosc):
        if nowa_pojemnosc == "":
            print("Pole nie może być puste")
        elif isinstance(nowa_pojemnosc, (str, float)):
            print("Pojemnosc nie może być literami ani zmiennoprzecinkowa")
        else:
            self._pojemnosc = nowa_pojemnosc


class Person:


    def __init__(self, imie="Unknown", nazwisko="Unknown", adres="Unknown"):
        self.lista_samochodow = []
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.garaz = Garage(adres,3)

    def __str__(self):
        opis = "Imie " + self.imie
        opis += "\nNazwisko " + self.nazwisko
        opis += "\nAdres " + self.adres
        opis += "\nGaraż " + str(self.garaz)
        return opis

    def dodaj_samochod_person(self, samochod):
        if len(self.lista_samochodow) < 4:
            self.lista_samochodow.append(samochod.numer_rejestracyjny)
            self.garaz.dodaj_samochod(samochod)
        else:
            print("Nie mozna mieć w garażu wiecej jak 3 samochody")

    def usun_samochod_person(self, numer_rejestracyjny):
        self.lista_samochodow.remove(numer_rejestracyjny)
        self.garaz.usun_samochod(numer_rejestracyjny)


class Car:
    licznik = 0

    def __init__(self, marka="Unknown", model="Unknown", drzwi=0, pojemnosc_silnika=0, numer_rejestracyjny="Unknown",
                 spalanie=0.0):
        self.marka = marka
        self.model = model
        self.drzwi = drzwi
        self.pojemnosc_silnika = pojemnosc_silnika
        self.numer_rejestracyjny = numer_rejestracyjny
        self.spalanie = spalanie
        Car.licznik += 1

    def __str__(self):
        opis = "Marka: " + self.marka
        opis += "\nModel: " + self.model
        opis += "\nIlość drzwi: " + str(self.drzwi)
        opis += "\nPojemność silnika: " + str(self.pojemnosc_silnika) + "ccm"
        opis += "\nNumer rejestracyjny: " + self.numer_rejestracyjny
        opis += "\nSpalanie: " + str(self.spalanie)
        return opis

    @staticmethod
    def liczba_obiektow():
        print("\nOgólna liczba obiektow to {0}.".format(Car.licznik))

    @property
    def marka(self):
        return self._marka

    @property
    def model(self):
        return self._model

    @property
    def drzwi(self):
        return self._drzwi

    @property
    def pojemnosc_silnika(self):
        return self._pojemnosc_silnika

    @property
    def numer_rejestracyjny(self):
        return self._numer_rejestracyjny

    @property
    def spalanie(self):
        return self._spalanie

    @marka.setter
    def marka(self, nowa_marka):
        if nowa_marka == "":
            print("To pole nie może być puste")
        elif isinstance(nowa_marka, (int, float)):
            print("Marka nie moze być samymi cyframi")
        else:
            self._marka = nowa_marka

    @model.setter
    def model(self, nowy_model):
        if nowy_model == "":
            print("Pole nie może być puste")
        else:
            self._model = nowy_model

    @drzwi.setter
    def drzwi(self, nowa_drzwi):
        if nowa_drzwi == "":
            print("Pole nie może być puste")
        elif isinstance(nowa_drzwi, (str)):
            print("Ilosc drzwi nie może być literami")
        elif isinstance(nowa_drzwi, (float)):
            print("Ilosc drzwi nie może być zmiennoprzecinkowa")
        else:
            self._drzwi = nowa_drzwi

    @pojemnosc_silnika.setter
    def pojemnosc_silnika(self, nowy_pojemnosc_silnika):
        if nowy_pojemnosc_silnika == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_pojemnosc_silnika, (str)):
            print("Pojemność silnika musi być cyfrą")
        else:
            self._pojemnosc_silnika = nowy_pojemnosc_silnika

    @numer_rejestracyjny.setter
    def numer_rejestracyjny(self, nowa_numer_rejestracyjny):
        if nowa_numer_rejestracyjny == "":
            print("Pole nie może byc puste")
        elif isinstance(nowa_numer_rejestracyjny, (int, float)):
            print("Pole nie może być cyfrą")
        else:
            self._numer_rejestracyjny = nowa_numer_rejestracyjny

    @spalanie.setter
    def spalanie(self, nowy_spalanie):
        if nowy_spalanie == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_spalanie, (str)):
            print("Spalanie nie może być literami")
        else:
            self._spalanie = nowy_spalanie

    def oblicz_spalanie(self, trasa, ilosc_paliwa):
        self.spalanie = (ilosc_paliwa / trasa) * 100
        print(self._spalanie)

    def oblicz_koszt(self, trasa, cena_paliwa):
        if self._spalanie == 0.0:
            print("Najpierw ustaw spalanie")
        else:
            print("{0:.2f}".format(trasa * (self._spalanie / 100) * cena_paliwa))


