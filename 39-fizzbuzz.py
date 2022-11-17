# Pytanie 39 - napisz program, który dla kolejnych liczb z zakresu od 1 do n:
# wypisze: "Fizz" - jeśli liczba będzie podzielna przez 3
# wypisze: "Buzz" - jeśli liczba będzie podzielna przez 5
# wypisze: "FizzBuzz" - jeśli liczba będzie podzielna przez 3 i 5
# jeśli nie zajdzie żaden z tych przypadków, to wypisz po prostu liczbę.

# def fizzbuzz(n):
#     for digit in range(1, n + 1):
#         if digit % 3 == 0 and digit % 5 == 0:
#             print('FizzBuzz')
#         elif digit % 5 == 0:
#             print('Buzz')
#         elif digit % 3 == 0:
#             print('Fizz')
#         else:
#             print(digit)

def fizzbuzz2(n):
    for num in range(1, n + 1):
        result = ''
        if num % 3 == 0:
            result += 'Fizz'
        if num % 5 == 0:
            result += 'Buzz'
        if num % 3 != 0 and num % 5 != 0:
            result = str(num)
        print(result)


fizzbuzz2(15)
