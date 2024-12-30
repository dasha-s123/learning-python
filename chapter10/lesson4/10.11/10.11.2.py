from time import sleep
import json

print('Привет!')
sleep(1)
print('Сейчас я угадаю твое любиме число!')
for sleep_count in range(3):
    sleep(1)
    print('.', end='')
sleep(1)
print()
with open('favorite_numer.json') as f:
    fav_number = json.load(f)
    print(f"Твое любимое число - {fav_number}, так?")
