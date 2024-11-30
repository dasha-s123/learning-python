def describe_city(city, country='Россия'):
    """выводит сообщение о местонахождении страны"""
    print(f'Город {city.title()} находится в стране {country.title()}')

describe_city('Липецк')
describe_city(city='берлин', country='германия')    #вызываю функции по-разному задавая значения
describe_city('париж', "франция")
