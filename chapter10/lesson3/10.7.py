def calculator_divide(number_one, number_two):
    """Калькулятор, позволяющий делить два числа"""
    try:
        int(number_one) / int(number_two)
    except ValueError:
        print('Вводите числа пожалуйста!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!\n')
    else:
        divide_result = int(number_one) / int(number_two)
        print(f'Частное ваших чисел - {divide_result}\n')



print('Введите два числа, а я их разделю')
print('(Нажмите "q" для выхода)')
while True:
    num_1 = input('\nПервое число: ')
    if num_1 == 'q':
        break
    num_2 = input('Второе число: ')
    if num_2 == 'q':
        break
    calculator_divide(num_1, num_2)