def is_even(number):
    """Проверяет число на четность"""

    return number % 2 == 0


number = int(input('Введите число, а я проверю его на четность: '))

parity = "четное" if is_even(number) else "нечетное"
print(f"\nВаше число - {number} и оно {parity}!")