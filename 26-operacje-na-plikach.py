# Pytanie 26
# - stwórz plik o nazwie "moj_plik.txt"
# - wpisz do niego liczb od 1 do 100, każdą w nowej linijce
# - otwórz plik i zapisz jego zawartosc do listy z_pliku

with open('moj_plik.txt', 'w') as f:
    for digit in range(1, 101):
        f.write(str(digit) + '\n')

with open('moj_plik.txt', 'r') as f:
    from_file = f.readlines()

print(from_file)

with open('moj_plik.txt', 'r') as f:
    z_pliku = []
    for line in f:
        z_pliku += [int(i) for i in line.split()]

print(z_pliku)

with open('moj_plik.txt', 'r') as f:
    file = f.read()

print(file)

# https://www.programiz.com/python-programming/file-operation
