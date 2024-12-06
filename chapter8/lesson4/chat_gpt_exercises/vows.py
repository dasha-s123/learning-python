def count_vowels(word):
    """Считает количество гласных в строке"""
    vowels = 'ауеыоэяию'

    # Проверка на количество гласных (добавляет в сумму 1 если буква - гласная)
    count_of_vowels = sum(1 for char in word if char.lower() in vowels)
    return count_of_vowels


string = input('Введите вашу строку: ')

print(f'\nВ вашей строке {count_vowels(string)} гласных!')