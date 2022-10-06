# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

def letter_dict_counter(sentence):
    new_dict = {}
    for letter in sentence:
        if letter not in new_dict.keys():
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    return new_dict


print(letter_dict_counter('myszydokazujągdykotanieczują'))
