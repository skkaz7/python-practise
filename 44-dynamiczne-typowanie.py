# Pytanie 45 - co to znaczy, że Python językiem dynamicznie typowanym?

a = 5
print(type(a))
a = 'pięć'
print(type(a))
a = [1, 2, 3]
print(type(a))

# aby używać type hints należy zainstalować i zaimportować bibliotekę typing
from typing import List


# def przeliteruj(word: str) -> List[str]:  # definicja funkcji, która pobiera arg typu string i zwraca listę stringów
#     return list(word)

def przeliteruj(word: str) -> List[str]:
    return 5


print(przeliteruj(1))

# print(przeliteruj('Python'))

# mypy - program, który pozwala analizować kod Pythona pod kątem poprawności przy założeniu statycznego typowania
# aby go użyć należy w konsoli wpisać: mypy nazwa_pliku_ktory_chcemy_przeanalizoac.pys

# https://docs.python.org/3/library/typing.html
# https://www.youtube.com/watch?v=2wDvzy6Hgxg
