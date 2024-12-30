import json

fav_num = input('Какое ваше любимое число? ')
with open("favorite_numer.json", 'w') as f:
    json.dump(fav_num, f)

print('Мы его запомнили!')