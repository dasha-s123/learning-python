def make_album(name_of_singer, name_of_album):
    """возвращает словарь с именем музыканта и названием альбома"""
    music = {"singer": name_of_singer.title(), "name": name_of_album}
    return music


print(make_album('noize', 'последний альбом')) #создаю и вывожу словари для разных альбомов
print(make_album('валентин стрыкало', 'смирись и расслабься'))
