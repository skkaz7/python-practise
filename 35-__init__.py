# Pytanie 35 - do czego w Pythonie służy __init__ ? Czym różni się od __init__.py ?
# Napisz fragment kodu wykorzystujący __init__.

class Pies:
    def __init__(self, imie, rasa):  # konstruktor klasy pobierający imię i rasę
        self.imie = imie
        self.rasa = rasa


maly_pies = Pies('Odi', 'sznaucer')
duzy_pies = Pies('Killer', 'doberman')  # tworzenie obiektu klasy Pies, z parametrami konstruktora "Killer" i 'doberman'

print(maly_pies.imie, maly_pies.rasa)  # wydrukowanie atrybutów obiektów
print(duzy_pies.imie, duzy_pies.rasa)

# __init__ to konstruktor klasy w pythonie; konstruktor klasy jest to metoda klasy która pozwala tworzyć obiekty danej klasy
# parametr self - słowo charakterystyczne dla programowania obiektowego w Pythonie;
# mówi nam, że metoda np. __init__ będzie działała na obiekcie, instancji danej klasy
