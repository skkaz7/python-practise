# Pytanie 3 - napisz kod, który zaprezentuje najważniejsze różnice między listą a tuplą

L = [1, 2, 3, True, (1, 2)]
T = (4, 5, 6, False, ['x', 'y'])

L[2] = 'trzy'
print(L)

T[2] = 'sześć'
# TypeError

"""
Zarówno lista i tupla (krotka) mogą zawierać różne typy danych
-listę zapisujemy w nawiasach kwadratowych []
-a tuplę w nawiasach okrągłych ()
-lista jest obiektem mutowalnym
-tupla jest obiektem niemutowalnym (nie możemy jej modyfikować)
"""

# https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
