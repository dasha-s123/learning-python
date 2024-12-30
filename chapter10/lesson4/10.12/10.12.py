import json
from time import sleep

try:
    print('Привет!')
    sleep(1)
    with open('favorite_number.json') as f:
        fav_numb = json.load(f)
except FileNotFoundError:
    with open('favorite_number.json', 'w') as f:
        fav_numb = input('Какой твой любимый номер? ')
        json.dump(fav_numb, f)
        sleep(1)
        print(f'Мы запомнили, что твое любимое число - {fav_numb}!')
else:
    print(f'Мне кажется, что твое любимое число - {fav_numb}!')