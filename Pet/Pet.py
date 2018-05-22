class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        value = self.hunger + self.tiredness
        if value < 6:
            print("Jestem happy :D")
        elif 6 < value < 11:
            print("No jest spoko")
        elif 10 < value < 16:
            print("Denerwuję się")
        elif value > 16:
            print("Teraz to już jestem mocno wkurzony")

    def talk(self):
        self._passage_of_time()
        self.mood

    def eat(self, food=4):
        self._passage_of_time()
        self.hunger -= food

    def play(self, zabawa=4):
        self._passage_of_time()
        self.tiredness -= zabawa

    def __str__(self):
        return "\nImie: {}\nGłód: {}\nZnudzenie: {} ".format(
            self.name, self.hunger, self.tiredness)


def main():
    name = input("Podaj imię zwierzaka: ")
    animal = Pet(name)
    print("To Twoje zwierzątko.",animal)
    input("Kliknij dowolny przycisk")
    clear()
    while(True):
        print("1. Nakarm zwierzaka\n2. Pobaw się ze zwierzakiem\n3. Jak się masz\n4. Wyjdź")
        chose = input()
        if chose == '1':
            print("Nakarm zwierzaka - podaj wartość jedzenia")
            animal.eat(int(input()))
            continue
        elif chose == '2':
            print("Jak długo chcesz się bawić? ")
            animal.play(int(input()))
            continue
        elif chose == '3':
            animal.talk()
            continue
        elif chose == "xy":
            print(animal)
            continue
        elif chose == '4':
            napis()
            break
        else:
            print("Zla opcja")
            continue
        break

def clear():
    print("\n" * 50)

def napis():
    print("""
     _  __  ____   _   _   _____  ______   _____
    | |/ / / __ \ | \ | | |_   _| | ____| / ____|
    | ' / | |  | ||  \| |   | |   | |__   | |
    |  <  | |  | || . ` |   | |   | __|   | |
    | . \ | |__| || |\  |  _| |_  | |____ | |____
    |_|\_\ \____/ |_| \_| |_____| |______| \_____|
     _____    _____  __     __
    / ____|  |  __ \ \ \   / /
    | |  __  | |__) | \ \_/ /
    | | |_ | | _   /   \   / 
    | |__| | | | \ \    | |
     \_____| |_|  \_\   |_|
    """)
main()
