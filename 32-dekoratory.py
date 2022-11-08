# Pytanie 32 - do czego w Pythonie służą dekoratory? Napisz dekorator, który będzie
# będzie dodawał trzy gwiazdki przed i po efekcie działania udekorowanej funkcji.

def add_stars(function):
    def decorated_function():
        print('***')
        function()
        print('***')

    return decorated_function()


@add_stars
def f():
    print('Hello World!')

# https://stackoverflow.com/questions/5929107/decorators-with-parameters

# dekorator -> funkcja, która jako argument pobiera inną funkcję w celu zmiany działania pobranej funkcji lub dodaniu
# do niej nowych funkcjonalności; udekorowanie pobranej funkcji w nowe właściwości
