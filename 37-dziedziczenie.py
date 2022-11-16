# Pytanie 37 - co zostanie wypisane w wyniku uruchomienia poniższego kodu?

class ZwierzeLadowe:
    def przedstaw_sie(self):
        print("Jestem zwierzęciem lądowym.")

    def biegaj(self):
        print("Biegam tu i tam.")


class ZwierzeMorskie:
    def przedstaw_sie(self):
        print("Jestem zwierzęciem morskim.")

    def plywaj(self):
        print("Pływam tu i tam.")


class SwinkaMorska(ZwierzeLadowe, ZwierzeMorskie):
    pass  # klasa ZwierzeLadowe lądowe ma priorytet nad klasą ZwierzeMorskie bo jest podana jako pierwsza


swinka = SwinkaMorska()
swinka.przedstaw_sie()  # wywołanie metody przedstaw_sie odziedziczonej z klasy ZwierzeLadowe
swinka.biegaj()
swinka.plywaj()

# https://www.programiz.com/python-programming/methods/built-in/super
