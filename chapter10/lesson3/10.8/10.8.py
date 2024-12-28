def file_reading(filename):
    """Читает содержимое файлов"""
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read().split()
    except FileNotFoundError:
        print(f'Файл с именем "{filename}" не найден')
    else:
        print(f'Содержимое файла с именем "{filename}":')
        for line in lines:
            print(line)
        print()


filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    file_reading(file)