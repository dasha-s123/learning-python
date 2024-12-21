from random import choice

lottery = ('1', 'A', '3', 'b', 'g', '9', '7', 'S')
print(f'Выигрышный билет - {choice(lottery) +
                            choice(lottery) +
                            choice(lottery) +
                            choice(lottery)}')