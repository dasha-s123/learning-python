user_name = input('Как вас зовут? ')

with open('user_name.txt', 'w') as file_object:
    file_object.write(user_name)