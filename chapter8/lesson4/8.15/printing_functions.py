def print_models(unprinted_designs, completed_designs):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Кая модель после печати перемещается в completed_designs
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Печатаем: {current_design}')
        completed_designs.append(current_design)

def show_completed_models(completed_designs):
    """Вывоит информацию обо всех напечатанных моделях"""
    print(f'\nБыли напечатаны:')
    for current_model in completed_designs:
        print(f'\t{current_model}')