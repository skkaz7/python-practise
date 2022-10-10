# Pytanie 20 - co otrzymamy w wyniku wydrukowania zawartości poniższych zmiennych?

L = [1, 2, 3, 4, 5, 6]

L1 = [x for x in range(5)]
L2 = [x ** 2 for x in L]
L3 = [x for x in L if x % 2 == 0]
L4 = ['Parzysta' if x % 2 == 0 else 'Nieparzysta' for x in range(5)]
L5 = [(x, x + 10) for x in L]
D1 = {x: x % 2 == 0 for x in L}

L11 = [0, 1, 2, 3, 4]
L22 = [1, 4, 9, 16, 25, 36]
L33 = [2, 4, 6]
L44 = ['Parzysta', 'Nieparzysta', 'Parzysta', 'Nieparzysta', 'Parzysta']
L55 = [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16)]
D11 = {1: False, 2: True, 3: False, 4: True, 5: False, 6: True}
