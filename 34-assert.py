# Pytanie 34 - napisz fragment kodu, w którym zobrazujesz użycie słowa kluczowego assert.
# Wyjaśnij jaka jest rola testów jednostkowych i czym charakteryzuje się dobry test jednostkowy.

def dodawanie(a, b):
    return a + b


def test_dodawanie_int():
    assert dodawanie(2, 2) == 4


def test_dodawanie_str():
    assert dodawanie('a', 'b') == 'ab'

# pytest    - framework do uruchamiania testów
# aby o zainstalowac nalezy w linii komend wpisać "pip install pytest"
# aby uruchomić testy wpisujemy: pytest nazwa_pliku.py

# unittest - moduł biblioteki standardowej służący do uruchamiania testów, działa podobnie jak pytest

# https://docs.pytest.org/en/latest/getting-started.html
