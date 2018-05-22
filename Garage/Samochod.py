class Garage:
    lista = []

    def __init__(self, adres="Unknown", pojemnosc=0, liczba_samochodow=0):
        self.__adres = adres
        self.__pojemnosc = pojemnosc
        self.__liczba_samochodow = liczba_samochodow

    def __str__(self):
        opis = "Adres: " + self.__adres
        opis += "\nPojemność: " + str(self.__pojemnosc)
        opis += "\nLiczba samochodów: " + str(self.__liczba_samochodow)
        for i in self.lista:
            opis += "\n"
            opis += str(i)
        return opis

    def dodaj_samochod(self, samochod):
        if self.__liczba_samochodow < self.__pojemnosc:
            self.lista.append(samochod)
            self.__liczba_samochodow += 1
        else:
            print("Brak miejsca w garażu")

    def usun_samochod(self, numer_rejestracyjny):
        for x in self.lista:
            if x.numer_rejestracyjny == numer_rejestracyjny:
                self.lista.remove(x)
                self.__liczba_samochodow -= 1

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, nowy_adres):
        if nowy_adres == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_adres, (float, int)):
            print("Adres nie moze być liczbą")
        else:
            self.__adres = nowy_adres

    @property
    def pojemnosc(self):
        return self.__pojemnosc

    @pojemnosc.setter
    def pojemnosc(self, nowa_pojemnosc):
        if nowa_pojemnosc == "":
            print("Pole nie może być puste")
        elif isinstance(nowa_pojemnosc, (str, float)):
            print("Pojemnosc nie może być literami ani zmiennoprzecinkowa")
        else:
            self.__pojemnosc = nowa_pojemnosc


class Person:
    lista_samochodow = []

    def __init__(self, imie="Unknown", nazwisko="Unknown", adres="Unknown", garaz=Garage()):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__adres = adres
        self.__garaz = garaz
        self.__garaz.adres = adres

    def __str__(self):
        opis = "Imie " + self.__imie
        opis += "\nNazwisko " + self.__nazwisko
        opis += "\nAdres " + self.__adres
        opis += "\nGaraż " + str(self.__garaz)
        return opis

    def dodaj_samochod_person(self, samochod):
        if len(self.lista_samochodow) < 4:
            self.lista_samochodow.append(samochod.numer_rejestracyjny)
            self.__garaz.dodaj_samochod(samochod)
        else:
            print("Nie mozna mieć w garażu wiecej jak 3 samochody")

    def usun_samochod_person(self, numer_rejestracyjny):
        self.lista_samochodow.remove(numer_rejestracyjny)
        self.__garaz.usun_samochod(numer_rejestracyjny)


class Car:
    __licznik = 0

    def __init__(self, marka="Unknown", model="Unknown", drzwi=0, pojemnosc_silnika=0, numer_rejestracyjny="Unknown",
                 spalanie=0.0):
        self.__marka = marka
        self.__model = model
        self.__drzwi = drzwi
        self.__pojemnosc_silnika = pojemnosc_silnika
        self.__numer_rejestracyjny = numer_rejestracyjny
        self.__spalanie = spalanie
        Car.__licznik += 1

    def __str__(self):
        opis = "Marka: " + self.__marka
        opis += "\nModel: " + self.__model
        opis += "\nIlość drzwi: " + str(self.__drzwi)
        opis += "\nPojemność silnika: " + str(self.__pojemnosc_silnika) + "ccm"
        opis += "\nNumer rejestracyjny: " + self.__numer_rejestracyjny
        opis += "\nSpalanie: " + str(self.__spalanie)
        return opis

    @staticmethod
    def liczba_obiektow():
        print("\nOgólna liczba obiektow to {0}.".format(Car.__licznik))

    @property
    def marka(self):
        return self.__marka

    @property
    def model(self):
        return self.__model

    @property
    def drzwi(self):
        return self.__drzwi

    @property
    def pojemnosc_silnika(self):
        return self.__pojemnosc_silnika

    @property
    def numer_rejestracyjny(self):
        return self.__numer_rejestracyjny

    @property
    def spalanie(self):
        return self.__spalanie

    @marka.setter
    def marka(self, nowa_marka):
        if nowa_marka == "":
            print("To pole nie może być puste")
        elif isinstance(nowa_marka, (int, float)):
            print("Marka nie moze być samymi cyframi")
        else:
            self.__marka = nowa_marka

    @model.setter
    def model(self, nowy_model):
        if nowy_model == "":
            print("Pole nie może być puste")
        else:
            self.__model = nowy_model

    @drzwi.setter
    def drzwi(self, nowa_drzwi):
        if nowa_drzwi == "":
            print("Pole nie może być puste")
        elif isinstance(nowa_drzwi, (str)):
            print("Ilosc drzwi nie może być literami")
        elif isinstance(nowa_drzwi, (float)):
            print("Ilosc drzwi nie może być zmiennoprzecinkowa")
        else:
            self.__drzwi = nowa_drzwi

    @pojemnosc_silnika.setter
    def pojemnosc_silnika(self, nowy_pojemnosc_silnika):
        if nowy_pojemnosc_silnika == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_pojemnosc_silnika, (str)):
            print("Pojemność silnika musi być cyfrą")
        else:
            self.__pojemnosc_silnika = nowy_pojemnosc_silnika

    @numer_rejestracyjny.setter
    def numer_rejestracyjny(self, nowa_numer_rejestracyjny):
        if nowa_numer_rejestracyjny == "":
            print("Pole nie może byc puste")
        elif isinstance(nowa_numer_rejestracyjny, (int, float)):
            print("Pole nie może być cyfrą")
        else:
            self.__numer_rejestracyjny = nowa_numer_rejestracyjny

    @spalanie.setter
    def spalanie(self, nowy_spalanie):
        if nowy_spalanie == "":
            print("Pole nie może być puste")
        elif isinstance(nowy_spalanie, (str)):
            print("Spalanie nie może być literami")
        else:
            self.__spalanie = nowy_spalanie

    def oblicz_spalanie(self, trasa, ilosc_paliwa):
        self.__spalanie = (ilosc_paliwa / trasa) * 100
        print(self.__spalanie)

    def oblicz_koszt(self, trasa, cena_paliwa):
        if self.__spalanie == 0.0:
            print("Najpierw ustaw spalanie")
        else:
            print("{0:.2f}".format(trasa * (self.__spalanie / 100) * cena_paliwa))
