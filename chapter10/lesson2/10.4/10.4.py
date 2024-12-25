# Очищаю файл от предыдущих данных
with open('users_book.txt', 'w') as file_object:
    file_object.write('')

while True:
    print('Как вас зовут?')
    user_name = input('(Нажмите "q" для выхода) ')
    if user_name == 'q':
        break
    else:
        promt = f'Привет, {user_name.title()}!'


    # Заношу данные в файл с приветствиями
    with open('users_book.txt', 'a') as file_object:
        file_object.write(f'{promt}\n')
        print()