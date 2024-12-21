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