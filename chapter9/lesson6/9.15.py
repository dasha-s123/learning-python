from random import choice

lottery = ('1', 'A', '3', 'b', 'g', '9', '7', 'S')
# Задает выигрышный билет
my_ticket = choice(lottery) + choice(lottery) + choice(lottery) + choice(lottery)
count = 0
user_ticket = None

# Проверяет, сколько попыток понадоилось на выгрыш
while user_ticket != my_ticket:
    count += 1
    user_ticket = choice(lottery) + choice(lottery) + choice(lottery) + choice(lottery)

# Выводит количество попыток победить
print(f"На нахождение выигрышной комбинации '{my_ticket}' потребовалось {count} попыток")
