# Pytanie 36 - wykorzystajmy klasę Pies i obiekt maly_pies z poprzedniego pytania.
# Co stanie się gdy wypiszemy print(maly_pies)?
# Co zrobiłbyś, aby wydrukowana w ten sposób informacja zawierała imie i rase psa?

class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

    def __str__(self):
        return f"{self.imie} - {self.rasa}"

    def __repr__(self):
        return f"Pies zwie się {self.imie}. Jest rasy {self.rasa}."


piesek = Pies('Odi', 'sznaucer')
print(piesek)
print(repr(piesek))

# __str__ metoda specjalna, magiczna, która ma w Pythonie z góry określoną funkcjonalność
# metoda __str__ służy do tworzenia reprezentacji tekstowej obiektów klasy

# https://www.educative.io/answers/what-is-the-repr-method-in-python
