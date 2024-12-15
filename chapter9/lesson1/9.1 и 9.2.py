class Restaurant():
    """Модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type, open = True):
        """Инициирует атрибуты названия и типа кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open

    def describe_restaurant(self):
        """Описывает ресторан"""
        print(f'\nНзвание ресторана {self.restaurant_name}\nТип кухни {self.cuisine_type}\n')

    def open_restaurant(self):
        if self.open:
            print(f'Ресторан открыт!\n')
        else:
            print(f'Ресторан закрыт!\n')


cafe_1 = Restaurant('first', 'european', open=False)

print(cafe_1.restaurant_name)
print(cafe_1.cuisine_type)
cafe_1.describe_restaurant()
cafe_1.open_restaurant()