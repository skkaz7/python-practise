# Pytanie 28 - jaki błąd popełniono w poniższym kodzie?
# Co zrobić aby go uniknąć?
# Stworz moduł kserokopiarka zawierający funkcję, która podany string wydrukuje dwa razy
# Użyj tej funkcji w kodzie poniżej

from drukarka import wydrukuj_imie as wydrukuj_imie_z_drukarki
from ksero import ksero


def wydrukuj_imie(imie):
    print(imie)


wydrukuj_imie("Marta")
wydrukuj_imie_z_drukarki("Marta")
ksero("można, jeszcze jak!")
