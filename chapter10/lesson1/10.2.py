filename = 'E:/GitHub/learning-python/text_files/learning_python.txt'

with open(filename) as file_object:
    """Файл содержит строки - возможности питона"""
    lines = file_object.readlines()
for line in lines:
    # Выводятся возможности С взятые с возможностей python-а
    print(line.strip().replace('python', 'C'))