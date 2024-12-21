from random import randint
from time import sleep

class Die():
    """Модель кубика"""
    def __init__(self, count_of_faces):
        """Инициирует отрибут количества бросков"""
        self.count_of_faces = count_of_faces

    def roll_die(self):
        print('Осуществляем бросок!')
        sleep(0.5)
        for dot in range(3):
            print('.', end='')
            sleep(1)
        print()
        print(f'Выпало {randint(1, self.count_of_faces)}')


cube_1 = Die(10)
cube_1.roll_die()