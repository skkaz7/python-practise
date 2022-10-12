# Pytanie 24 - co zostanie wypisane w wyniku wykonania poniższego kodu?

A = [1, 2, 3, 4, 5]  # do zmiennej A przypisujemy REFERENCJĘ do przechowywanej w pamięci listy
B = A  # do zmiennej B przepisujemy REFERENCJĘ do listy przechowywanej pod zmienną A.
C = A[:]  # C = list(A)  # do zmiennej C przypisujemy KOPIĘ listy przechowywanej pod zmienną A
B[0] = 111  # zmieniamy pierwszy element listy, na który wskazują zarówno zmienne B jak i A

print(B)
print(A)
print(C)

print(id(B))  # drukujemy identyfikator obiektu przechowywanego pod zmienną B
print(id(A))  # drukujemy identyfikator obiektu prezchowywanego pod zmienną A (identyczny jak dla B)
print(id(C))  # drukujemy identyfikator obiektu przechowywanego pod zmienną C (inny niż dla A i B)

# https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
