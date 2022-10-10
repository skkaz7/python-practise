# Pytanie 16 - wypisz podaną listę imion przed każdym dodając kolejny numer.
# Zacznij numerowanie od 1.

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

for index, name in enumerate(imiona, 1):
    print(index, name)

# https://www.programiz.com/python-programming/methods/built-in/enumerate
