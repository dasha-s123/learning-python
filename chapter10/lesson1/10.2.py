filename = 'E:/GitHub/learning-python/chapter10/lesson1/10.1/learning_python.txt'

with open(filename) as file_object:
    """Файл содержит строки - возможности питона"""
    lines = file_object.readlines()
for line in lines:
    # Выводятся возможности С взятые с возможностей python-а
    print(line.strip().replace('python', 'C'))