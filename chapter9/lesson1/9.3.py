class User:
    """Модель пользователя"""

    def __init__(self, first_name, last_name, nickname, age=None, gender=None):
        """Инициирует обязательные атрибуты мени, фамилии и ника"""
        """И необязательные атрибуты возраста и пола"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f'Информация о {self.nickname}:')
        print(f'\tИнициалы - {self.first_name} {self.last_name}')
        if self.age:
            print(f'\tВозраст - {self.age} лет')
        if self.gender:
            print(f'\tГендер - {self.gender}')

    def greet_user(self):
        print(f'Здраствуйте, {self.first_name}! Мы рады вас видеть!')
        print()


user_1 = User('Даша', "Севостьянова", "Shypiece", 17, "женщина")
user_1.describe_user()
user_1.greet_user()

user_2 = User('Анна', "Карташова", "zill", 17)
user_2.describe_user()
user_2.greet_user()

user_3 = User('Гарник', "Геворгян", "garnik", gender='мужчина')
user_3.describe_user()
user_3.greet_user()