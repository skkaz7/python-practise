# Pytanie 42 - przy użyciu wyszukiwania binarnego sprawdź czy liczba 341 znajduje się w posortowanej liście P

arr = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]

searched_number = 341
left = 0
right = len(arr) - 1

while left <= right:
    middle = (left + right) // 2
    if arr[middle] == searched_number:
        print(f'Liczba {searched_number} znajduje się na liście')
        break
    elif arr[middle] < searched_number:
        left = middle + 1
    else:
        right = middle - 1
else:
    print(f'Liczba {searched_number} nie znajduje się na liście')

# https://pl.wikipedia.org/wiki/Wyszukiwanie_binarne

"""
Wyszukiwanie binarne – algorytm opierający się na metodzie dziel i zwyciężaj, który w czasie logarytmicznym stwierdza,
czy szukany element znajduje się w uporządkowanej tablicy
"""
