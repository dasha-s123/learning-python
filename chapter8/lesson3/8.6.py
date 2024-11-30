def city_country(city, country):
    """выдает сообщение вида: город, страна"""
    message = f'{city}, {country}'
    return message.title()


city = input("Введите название города: ") #запрашиваю аргументы у пользователей
country = input("Введите название страны: ")
promt = city_country(city, country) #использую эти аргументы при выводе функции
print(f'\t{promt}')