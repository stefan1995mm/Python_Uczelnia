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
        for x, y in self.marks.items():
            print(x + "\t\t" + str(y))

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


class Student(Pupil):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)
        self.weights = {}

    def complete_weights(self, przedmiot, waga):
        if 0 < waga <= 1:
            self.weights[przedmiot] = waga
        else:
            print("Zla waga")

    def mean(self):
        weights = 0
        marks = 0
        for key, value in self.marks.items():
            if key in self.weights.keys():
                weights += self.weights[key]
                marks += self.marks[key] * self.weights[key]
            else:
                print("Brak oceny")
        return marks / weights

    def __str__(self):
        opis = "Imie " + super().__str__()
        return opis
