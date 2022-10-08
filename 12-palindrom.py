# Pytanie 12 - napisz funkcję sprawdzającą czy podane słowo jest palindromem.
# Uruchom funkcję aby sprawdzić czy palindromami są słowa "kajak" i "anakonda".

def palindrome(phrase):
    return True if phrase == phrase[::-1] else False


print(palindrome('kajak'))
print(palindrome('anakonda'))

# https://stackoverflow.com/questions/199184/how-do-i-check-if-a-number-is-a-palindrome
