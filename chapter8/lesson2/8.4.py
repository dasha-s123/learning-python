def make_shirt(size=50, text="I love python"):
    """Выводит информацию о заказанной футболке"""
    print('Заказ офорлен')
    print(f'\tРазмер вашей футболки {size}')
    print(f'\tМы напишем на ней текст "{text}"')

make_shirt() #вызываю функцию, в которой значения по умолчанию
make_shirt(size=42) #вызываю функцию, где только 1 значение по умолчанию
