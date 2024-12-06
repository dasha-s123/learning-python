import math

def factorial(n):
    """Вычисляет факториал числа"""
    return math.factorial(n)


number = int(input('Введите ваше число: '))
if number < 0:
    print('\nФакториал определн только для неотрицательных чисел!')
else:
    result = factorial(number)
    print(f'\nФакториал вашего числа - {result}')
