import json


def get_stored_username():
    """Получает имя пользователя, если оно существует"""
    try:
        with open("user_name.json") as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое име пользователя"""
    username = input('Введите ваше имя: ')
    with open("user_name.json", 'w') as f:
        json.dump(username, f)
    return username


def check_username():
    """Проверяет соответствие пользователя"""
    username = get_stored_username()
    print(f"Ваше имя - {username}?")
    check = input('(да/нет) ')
    if check == 'да':
        return True
    else:
        print('Нам очень жаль!')
        return False

def greet_user():
    """Приветсвует пользователя"""
    username = get_stored_username()
    if username and check_username():
        print(f'Приветствую вас, {username}')
    else:
        username = get_new_username()
        print(f"Мы запомнили вас, {username}")


greet_user()