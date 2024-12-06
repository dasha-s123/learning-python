from sympy import isprime

def prime_numbers(limit):
    """Выводит все простые числа до ввденного"""
    return [number for number in range(2, limit +1) if isprime(number)]


user_number = int(input("Введите ваше число: "))
print(f'\nВот список простых чисел до вашего числа:\n{prime_numbers(user_number)}')