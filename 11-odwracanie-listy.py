# Pytanie 11 - na podstawie listy jezyki stworz listę jezyki_odwrocone
# zawierającą elementy listy jezyki w odwroconej kolejnosci

langs = ['python', 'java', 'c#', 'ruby']
print(langs)

# 1
langs_reversed = langs[::-1]
print(langs_reversed)

# 2
langs_reversed2 = list(reversed(langs))
print(langs_reversed2)

# 3
# langs.reverse()
# print(langs)

# 4
langs_reversed3 = []
for lang in langs:
    langs_reversed3.insert(0, lang)
print(langs_reversed3)
