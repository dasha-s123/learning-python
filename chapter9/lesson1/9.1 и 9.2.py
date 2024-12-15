class Restaurant:
    """Модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type, open = True):
        """Инициирует атрибуты названия и типа кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open

    def describe_restaurant(self):
        """Описывает ресторан"""
        print(f'Нзвание ресторана {self.restaurant_name}\nТип кухни {self.cuisine_type}')

    def open_restaurant(self):
        if self.open:
            print(f'Ресторан открыт!')
        else:
            print(f'Ресторан закрыт!')


cafe_1 = Restaurant('first', 'Европейская', open=False)
cafe_2 = Restaurant('Чили', 'Мексиканская')
cafe_3 = Restaurant('Оживи', 'кофейня', open=True)
cafe_4 = Restaurant('Dodo пицца', 'пиццерия', False)
# Список всех рестаранов города
restaurants = [cafe_1, cafe_2, cafe_3, cafe_4]

# Выводит всю информацию о ресторанах
for current_cafe in restaurants:
    print(current_cafe.restaurant_name)
    print(current_cafe.cuisine_type)
    current_cafe.describe_restaurant()
    current_cafe.open_restaurant()
    print()