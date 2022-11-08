"""
generator -> rodzaj funkcji, która zwraca obiekt zwany iteratorem. Iterator to obiekt po którym możemy iterować (one value at a time)
1) oszczędzanie pamięci
2) używane do sekwencji, które nie mają końca
3) słowo kluczowe yield
"""


def return_next_even():
    for n in range(2, 20, 2):
        yield n


# for item in return_next_even():
#     print(item)

generator_object = return_next_even()
print(generator_object)

for i in range(10):
    print(next(generator_object, None))

y = ('a' * n for n in range(1, 6))  # generator expression - wyrażenie generatorowe
# tworzy generator, który będzie zwracał kolejne wielokrotności stringa 'a' w zakresie od 1 do 5

for i in range(5):  # wypisanie kolejnych wartości zwróconych przez obiekt genratora y
    print(next(y))

# https://www.programiz.com/python-programming/generator
