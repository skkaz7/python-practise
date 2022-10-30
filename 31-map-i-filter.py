# Pytanie 31
# Otrzymujesz listę nazwisk jakie klienci wprowadzili w formularz na stronie internetowej.
# - użyj funkcji filter(), aby usunąć z niego wszystkie wpisy, które nie są stringami
# - użyj funkcji map() aby przerobić nazwiska tak, żeby wszystkie były zapisane poprawnie
# z wielkimi literami tylko na początku imienia i nazwiska.

nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK', ['nie', 'wasza', 'sprawa'], 'ROBERT wąŻ']

# filter(funkcja,sekwencja)
# elementy z listy nazwiska przekazywane są do lambdy, która sprawdza czy ich typ to string
# jeśli tak, to element zostaje dodany do listy nazwiska_filter

nazwiska_filter = list(filter(lambda x: type(x) is str, nazwiska))
print(nazwiska_filter)

# nazwiska_filter_2 = [x for x in nazwiska if type(x) is str]
# print(nazwiska_filter_2)

# map(funkcja,sekwencja)
# elementy z listy nazwiska_filter przekazane są do lambdy
# która najpierw zamienia wszystkie litery danego stringa na małe,
# a następnie pierwsza literę każdego słowa zmienia na dużą
# tak zmodyfikowany string zostaje dodany do listy nazwiska_map

nazwiska_map = list(map(lambda x: x.lower().title(), nazwiska_filter))
print(nazwiska_map)

# nazwiska_map_2 = [x.lower().title() for x in nazwiska_filter]
# print(nazwiska_map_2)

# https://www.programiz.com/python-programming/methods/built-in/filter
# https://www.programiz.com/python-programming/methods/built-in/map
# https://stackoverflow.com/questions/10973766/understanding-the-map-function
