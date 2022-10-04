# Pytanie 6 - jakiej struktury danych użyłbyś do zapisania numerów telefonów
# wszystkich klientów firmy i odpowiadających im nazwisk. Wybierz strukturę tak,
# aby sprawdzenie właściciela numeru telefonu nie zajmowało dużo czasu.

# Następnie stwórz przykładową strukturę przechowującą poniższe informacje:
# 123456789 - Jan Kot
# 999888777 - Anna Lis
# 111222333 - Jan Kot
# Odczytaj nazwisko właściciela numeru 123456789

new_dict = {
    123456789: 'Jan Kot',
    999888777: 'Anna Lis',
    111222333: 'Jan Kot'
}

# złożoność obliczeniowa wyszukania elementu w liście N-elementowej: O(N)
# złożoność obliczeniowa wyszukania elementu w słowniku N-elementowym: O(1) - lepsza!

print(new_dict[123456789])

# https://pl.wikipedia.org/wiki/Tablica_mieszaj%C4%85ca
