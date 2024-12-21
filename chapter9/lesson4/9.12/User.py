class User:
    """Модель пользователя"""

    def __init__(self, first_name, last_name, nickname, login_attemps=0, age=None, gender=None):
        """Инициирует обязательные атрибуты мени, фамилии и ника"""
        """И необязательные атрибуты возраста и пола"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.login_attemps = login_attemps
        self.age = age
        self.gender = gender
        self.new = None

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f'\nИнформация о {self.nickname}:')
        print(f'\tИнициалы - {self.first_name} {self.last_name}')
        if self.age:
            print(f'\tВозраст - {self.age} лет')
        if self.gender:
            print(f'\tГендер - {self.gender}')

    def greet_user(self):
        print(f'Здраствуйте, {self.first_name}! Мы рады вас видеть!')

    def show_login_attemps(self):
        """Показывает количество входов"""
        print(f"{self.new + ' ' if self.new else ''}{'к' if self.new else 'К'}оличество входов - {self.login_attemps}")

    def increment_login_attemps(self):
        """Увеличивает количество попыток вхда на 1"""
        self.login_attemps += 1
        self.new = 'Теперь'

    def reset_login_attemps(self):
        """Обнуляет количество попыток входа"""
        self.login_attemps = 0
        self.new = 'Теперь'