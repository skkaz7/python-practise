with open('tekstowy.txt', 'w') as f:
    f.write('Lubię placki')

with open('tekstowy.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('tekstowy.txt', 'a') as f:
    f.write('\n' + 'jeszcze jak!')

with open('/home/skkaz7/Pulpit/to_do', 'r') as f:
    print(f.read())

f = open('nowy.txt', 'w', encoding='utf-8')
f.write('Python')
f.close()

try:
    f = open('nowy.txt', 'r')
    print(f.read())
finally:
    f.close()
