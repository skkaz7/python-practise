# Pytanie 17 - znajdź różnicę między największą a najmniejszą wartością
# na poniższej liście.
# Zadbaj o to aby rozwiązanie było efektywne.

A = [4, 5, 7, -3, 2, 8, -10, 15]


def mini_maxi(lst):
    return max(lst) - min(lst)


print(mini_maxi(A))

# https://www.programiz.com/python-programming/methods/built-in/min
# https://www.programiz.com/python-programming/methods/built-in/max
