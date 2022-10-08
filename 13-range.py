# Pytanie 13
# stwórz dwie listy:
# A - zawierającą liczby od 1 do 10
# B - zawierającą co trzecią liczbę z zakresu od 100 do 1
# w obu przypadkach możesz napisać tylko jedną linijkę kodu

lst1 = [x for x in range(1, 11)]
# lst1 = list(range(1, 11))
print(lst1)
lst2 = [x for x in range(100, 0, -3)]
# lst2 = list(range(100, 0, -3))
print(lst2)

# Python 2.x - range był funkcją - zwracał listę (xrange - działał jak range w Pythonie 3.x)
# Python 3.x - range jest typem danych - zwraca sekwencję liczb

# https://docs.python.org/3/library/stdtypes.html#range
