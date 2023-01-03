# Pytanie 40 - ciąg Fibonacciego to ciąg liczb, którego:
# - zerowy element wynosi 0
# - pierwszy element wynosi 1
# - każdy kolejny element jest sumą dwóch poprzedzających go elementów.
# Napisz funkcję, która zwróci n-ty element ciągu Fibonacciego.

# kolejny element ciągu: 0   1   2   3   4   5   6    7   8   9  10
# wartość dla elementu:  0   1   1   2   3   5   8   13  21  34  55

def fibonacci_r(n):  # O(2 ^ n)
    if n <= 1:
        return n
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)


if __name__ == '__main__':
    print(fibonacci_r(10))


def fibonacci_l(n):  # O(n)
    pierwsza, druga = 0, 1
    for _ in range(n):
        pierwsza, druga = druga, pierwsza + druga
    return pierwsza


if __name__ == '__main__':
    print(fibonacci_l(10))
