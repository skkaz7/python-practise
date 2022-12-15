# Pytanie 1 - lista niepowtarzalnych elementów
# Korzystając z podanej listy A
# stwórz listę B zawierającą tylko unikalne elementy z listy A

A = [1, 2, 3, 3, 2, 1, 2, 3]


def unique_elements_list(array):
    """
    param array: array with unordered elements
    return: array with unique elements
    """
    # result = []
    # for element in array:
    #     if element not in result:
    #         result.append(element)
    # return result
    result = []
    [result.append(x) for x in array if x not in result]
    return result


print(unique_elements_list(A))


# zwróć listę na podstawie setu stworzonego na podstawie listy A
def unique_elements_list_2(array):
    return list(set(A))


print(unique_elements_list_2(A))

# https://www.programiz.com/python-programming/set
