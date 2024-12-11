def car_information(mark, model, **car):
    """Строит словарь с характеристиками машины"""
    car['производитель'] = mark.title()
    car['модель'] = model.title()
    return car


my_car = car_information('subaru', 'outback', цвет='синий', тюннинг=True)
print(my_car)