class Pupil:
    def __init__(self, imie, nazwisko):
        self.__name = imie
        self.__surname = nazwisko
        self.__marks = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nowe_imie):
        if nowe_imie == "":
            print("Imie nie moze byc puste")
        elif isinstance(nowe_imie, (float, int)):
            print("Imie nie moze byc cyfrą")
        elif len(nowe_imie) < 3:
            print("Imie musi mieć conajmniej 3 znaki")
        else:
            self.__name = nowe_imie

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, nowe_nazwisko):
        if nowe_nazwisko == "":
            print("Nazwisko nie moze byc puste")
        elif isinstance(nowe_nazwisko, (float, int)):
            print("Nazwisko nie moze byc cyfra")
        elif len(nowe_nazwisko) < 3:
            print("Nazwisko musi mieć conajmniej 3 znaki")
        else:
            self.__surname = nowe_nazwisko

    def print_marks(self):
        for x in self.__marks.keys():
            print(x + "\t\t" + str(self.__marks[x]))

    def mean(self):
        mean = 0
        for x in self.__marks.values():
            mean += x
        return (mean / len(self.__marks))

    def complete_marks(self, nowa_ocena, liczba):
        if isinstance(nowa_ocena, str) and isinstance(liczba, (int, float)):
            self.__marks[nowa_ocena] = liczba
        else:
            print("Podales zle dane")

    def __str__(self):
        opis = "Imie: " + self.__name + "\n"
        opis += "Nazwisko: " + self.__surname + "\n"
        opis += "Srednia ocen: " + str(self.mean())
        return opis


klasa = Pupil("Jan", "Kowalski")
# klasa.name = ""
# print(klasa.name)
# klasa.name = 3
# print(klasa.name)
# klasa.name = "ja"
# print(klasa.name)
# klasa.name = "Andrzej"
# print(klasa.name)
# klasa.surname = ""
# print(klasa.surname)
# klasa.surname = 3
# print(klasa.surname)
# klasa.surname = "ja"
# print(klasa.surname)
# klasa.surname = "Nowak"
# print(klasa.surname)
klasa.print_marks()
klasa.complete_marks("Polski", 4)
klasa.complete_marks(3, "ang")
klasa.complete_marks("test", "ang")
klasa.complete_marks(3, 5)
print(klasa)
