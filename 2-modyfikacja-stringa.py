# Pytanie 2 - co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"
print(a[1])
# a[1] = 'X'             # próba modyfikacji stringa - operacja zabroniona skutkująca TypeError

a_lista = list(a)
a_lista[1] = 'X'
a = "".join(a_lista)  # metoda join
print(a)

# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

"""
1) struktury mutowalne, modyfikowalne - takie, które można zmieniać np. lista, słownik, set.
2) struktury niemutowalne, niemodyfikowalne - raz stworzony obiekt, musi pozostać w takiej formie, no. string, tupla.
"""
