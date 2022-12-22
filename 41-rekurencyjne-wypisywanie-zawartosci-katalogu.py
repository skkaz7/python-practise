# Pytanie 41 - napisz funkcję, która dla podanego katalgu wypisze znajdujące się w nim pliki.
# Pamiętaj, że katalog może zawierać podkatalogi, do których funkcja również musi zajrzeć.

# os.listdir - zwraca zawartość danego katalogu
# os.path.join - łączy dwa stringi w ścieżkę czytelną dla danego systemu operacyjnego
# os.path.isdir - sprawdza czy pod nadą ściezką znajduje się katalog

import os


def print_directory(directory_path):
    for element in os.listdir(directory_path):
        element_path = os.path.join(directory_path, element)
        if os.path.isdir(element_path):
            print_directory(element_path)
        else:
            print(element_path)


print_directory(r"/home/skkaz7/workspace/python-practise/testowy")

# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.path.html
