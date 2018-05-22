class Pupil:
    def __init__(self, imie, nazwisko):
        self.name = imie
        self.surname = nazwisko
        self.marks = {}
        self.oceny = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nowe_imie):
        if nowe_imie == "":
            print("Imie nie moze byc puste")
        elif isinstance(nowe_imie, (float, int)):
            print("Imie nie moze byc cyfrą")
        elif len(nowe_imie) < 3:
            print("Imie musi mieć conajmniej 3 znaki")
        else:
            self._name = nowe_imie

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, nowe_nazwisko):
        if nowe_nazwisko == "":
            print("Nazwisko nie moze byc puste")
        elif isinstance(nowe_nazwisko, (float, int)):
            print("Nazwisko nie moze byc cyfra")
        elif len(nowe_nazwisko) < 3:
            print("Nazwisko musi mieć conajmniej 3 znaki")
        else:
            self._surname = nowe_nazwisko

    def print_marks(self):
        for x in self.marks.keys():
            print(x + "\t\t" + str(self.marks[x]))

    def mean(self):
        mean = 0
        for x in self.marks.values():
            mean += x
        return (mean / len(self.marks))

    def complete_marks(self, nowa_ocena, liczba):
        if isinstance(nowa_ocena, str) and isinstance(liczba, (int, float)) and liczba in self.oceny:
            self.marks[nowa_ocena] = liczba
        else:
            print("Podales zle dane")

    def __str__(self):
        opis = "Imie: " + self.name + "\n"
        opis += "Nazwisko: " + self.surname + "\n"
        opis += "Srednia ocen: " + str(self.mean())
        return opis


class Student:


# klasa = Pupil("J",3)
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
# klasa.print_marks()
# klasa.complete_marks("Polski", 4.2)
# klasa.complete_marks(3, "ang")
# klasa.complete_marks("test", "ang")
# klasa.complete_marks(3, 5)
klasa.complete_marks("Polski", 4)
klasa.complete_marks("Angielski", 3)
klasa.complete_marks("Matematyka", 3.5)
klasa.complete_marks("Fizyka", 6)
# klasa.print_marks()
print(klasa)
