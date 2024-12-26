while True:
    print('Почему вы программируете?')
    user_reason = input('(Нажмите "q" для выхода) ')
    if user_reason == 'q':
        break
    else:
        reason = f'Человек программирует, потому что: "{user_reason}"'

    with open('reasons_for_programming.txt', 'r+') as file_object:
        if file_object.readline() != 'Причины, по которым люди программируют:\n\n':
            file_object.write('Причины, по которым люди программируют:\n\n')

    with open('reasons_for_programming.txt', 'a') as file_object:
        file_object.write(f'{reason}\n')
    print()