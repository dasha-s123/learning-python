def word_count(filename, word):
    """Считает количество вхождений слова в текст"""
    try:
        with open(filename, encoding='utf-8') as f:
            count_of_word = f.read().count(str(word))
    except FileNotFoundError:(
        print(f'Файл с именем "{filename}" не найден'))
    else:
        print(f'Число вхождений "{word}" - {count_of_word}')


word_count('alice_in_wonderland.txt', 'the ')