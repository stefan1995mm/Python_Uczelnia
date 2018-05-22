class Pupil:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.marks = {}
        self.oceny = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, new_imie):
        if len(new_imie) >= 3:
            self._imie = new_imie
        else:
            self._imie = "Nieznane"

    @imie.getter
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, new_nazwisko):
        if len(new_nazwisko) >= 3:
            self._nazwisko = new_nazwisko
        else:
            self._nazwisko = "Nieznane"

    @nazwisko.getter
    def nazwisko(self):
        return self._nazwisko

    def complete_marks(self, przedmiot, ocena):
        if ocena in self.oceny:
            self.marks[przedmiot] = ocena
        else:
            print("Błędna ocena")

    def print_marks(self):
        for key, mark in self.marks:
            print(key, ": ", mark)

    def mean(self):
        sum = 0
        for key, mark in self.marks.items():
            sum += mark
        return sum / len(self.marks)

    def __str__(self):
        return "Imie: " + self.imie + " Nazwisko: " + self.nazwisko + " Srednia: " + str(self.mean())


class Student(Pupil):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)
        self.weights = {}

    def complete_weights(self, przedmiot, waga):
        if 0 < waga <= 1:
            self.weights[przedmiot] = waga
        else:
            print("Podano złą wagę przedmiotu")

    def mean(self):
        sum_with_weights = 0
        sum_weights = 0
        for key, mark in self.marks.items():
            if key not in self.weights:
                sum_with_weights += mark
                sum_weights += 1
            else:
                sum_with_weights += mark * self.weights[key]
                sum_weights += self.weights[key]
        return sum_with_weights / sum_weights

    def __str__(self):
        return super().__str__()


student1 = Student("tak", "Andrzej")
student1.complete_weights("polski", 1)
student1.complete_marks("polski", 4)
student1.complete_weights("matematyka", 0.1)
student1.complete_marks("matematyka", 2)
print(student1)
# student1.imie="kt"
print(student1.imie)
