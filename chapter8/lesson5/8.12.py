def user_sandwich(*components):
    """Выводит все компоненты сендвича"""
    print('Вы заказали сендвич с начинками:')
    for ingredient in components:
        print(f'\t{ingredient}')
    print()


user_sandwich('сыр', 'салат', 'бородинский хлеб')
user_sandwich('мясо', 'салат')
user_sandwich('помидоы', 'соус', 'огурец', 'яйчо')