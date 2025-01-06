def place_formatted_name(city, country, population = ''):
    """Форматирует место по виду 'Город, Страна - популяция' (если данные о популяции есть"""
    if population:
        place = f"{city.title()}, {country.title()} - population {population}"
    else:
        place = f"{city.title()}, {country.title()}"
    return place
