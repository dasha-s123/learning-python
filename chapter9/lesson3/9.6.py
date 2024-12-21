class Restaurant:
    """Модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type, open=True):
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

    def set_number_served(self, number_served):
        """Определяет число посетителей"""
        self.number_served = number_served

    def show_number_served(self):
        """Выводит число посетителей"""
        print(f'За сегодня обслужено {self.number_served} человек(а)')

    def increasement_number_served(self, new_people):
        """Обновляет число посетителей"""
        self.number_served += new_people


class IceCreamStand(Restaurant):
    """Создает модель киоска с мороженным"""

    def __init__(self, restaurant_name, cuisine_type, *flavors, open=True):
        """Инициирует атрибуты киоска"""
        # Добавляет атрибут вкуса мороженного
        self.flavors = flavors
        # Атрибуты киоска как ресторана
        super().__init__(restaurant_name, cuisine_type, open)

    def show_flavors(self):
        """Выводит описание вкусов мороженного"""
        print('В киоске есть следующие вкусы мороженного:')
        for flavor in self.flavors:
            print(f'\t{flavor}')


ice_cream_cafe_1 = IceCreamStand('Пингвин', 'мороженное',
                                 'ваниль', 'клубника', 'шоколад',
                                 open=False)

ice_cream_cafe_1.describe_restaurant()
ice_cream_cafe_1.set_number_served(4)
ice_cream_cafe_1.show_number_served()
ice_cream_cafe_1.show_flavors()
ice_cream_cafe_1.open_restaurant()
