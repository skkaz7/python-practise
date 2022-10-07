# Pytanie 10 - korzystając ze słownika stworzonego w poprzednim zadaniu
# sprawdź czy któraś z liter wystąpiła w stringu dokładnie 4 razy.
# Jeśli tak - wypisz True, jeśli nie - False.

dic = {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, 'k': 2, 'a': 2, 'u': 2,
       'j': 2, 'ą': 2, 'g': 1, 't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}

print(dic.values())  # wydrukuje obiekt dict_values zawierający wartości słownika
print(list(dic.values()))  # drukuje listę stworzoną na podstawie obiektu dict_values

for key in dic.keys():
    if dic[key] == 4:
        print(True)

print(True if 4 in dic.values() else False)

# https://www.programiz.com/python-programming/methods/dictionary/values

print(sum(dic.values()))
