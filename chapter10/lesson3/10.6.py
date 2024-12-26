first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')

try:
    int(first_number) and int(second_number)
except ValueError:
    print('\nВведите два числа!')
else:
    summa = int(first_number) + int(second_number)
    print(f'\nСумма ваших чисел - {summa}')
