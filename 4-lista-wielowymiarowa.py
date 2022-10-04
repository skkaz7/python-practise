# Pytanie 4 - jakiej struktury danych użyłbyś do zamodelowania
# szafki, która ma 3 szuflady, a w każdej z nich 3 przegródki?
# Stwórz taki model i umieść stringa "długopis"
# w środkowej przegródce środkowej szuflady.

szafka = [[[1], [2], [3]], [[1], [2], [3]], [[1], [2], [3]]]

szafka[1][1] = 'długopis'
print(szafka)
print()
for szuflada in szafka:
    print(szuflada)

# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
