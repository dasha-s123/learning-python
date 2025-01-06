def place_formatted_name(city, country):
    """Форматирует место по виду 'Город, Страна'"""
    place = f"{city.title()}, {country.title()}"
    return place