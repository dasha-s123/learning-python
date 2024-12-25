filename = 'learning_python.txt'

with open(filename) as file_object:
    """Файл содержит строки - возможности питона"""
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print()


with open(filename) as file_object:
    reasons = file_object.read()
    print(reasons.rstrip())
print()


with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())