# Pytane 38 - do czego służą dekoratory @staticmethod i @classmethod?

class Matematyka:
    def __init__(self):
        self.pi = 3.14

    def policz_obwod_okregu(self, r):
        return round(2 * self.pi * r, 2)

    @staticmethod  # metoda statyczna nie jest swiadoma bycia czescia klasy, a wiec nie widzi innych metod tej klasy
    def dodaj(a, b):
        return a + b

    # @staticmethod
    # def dodaj_i_pomnoz(a, b):
    #     return dodaj(a, b) * 2

    @classmethod  # metoda klasowa jest swiadoma bycia czescia klasy i widzi inne metody w klasie; wymaga slowa kluczowego cls (zamiast self) bo operuje na klasie a nie na jej obiekcie/instancji
    def dodaj_i_pomnoz(cls, a, b):
        return cls.dodaj(a, b) * 2


m = Matematyka()
print(m.policz_obwod_okregu(5))
print(Matematyka.dodaj(2, 3))
print(Matematyka.dodaj_i_pomnoz(2, 3))
