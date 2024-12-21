import User

"""Классы моделирующие админ его привеии"""


class Privileges():
    """Модель списка привелегий"""

    def __init__(self):
        """Инициирует привелегии"""
        self.privileges = None

    def determine_privileges(self, *priveleges):
        self.privileges = priveleges

    def show_privileges(self):
        print(f'Администратор может:')
        for right in self.privileges:
            print(f'\t{right}')


class Admin(User.User):
    """Создает модель администратора"""

    def __init__(self, first_name, last_name, nickname, login_attemps=0, age=None, gender=None):
        super().__init__(first_name, last_name, nickname, login_attemps, age, gender)
        self.privileges = Privileges()
