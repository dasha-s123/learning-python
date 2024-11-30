def make_album(name_of_singer, name_of_album, count_of_songs=None):
    """возвращает словарь с именем музыканта и названием альбома"""
    music = {"singer": name_of_singer.title(), "name": name_of_album}
    if count_of_songs:
        music["count_of_songs"] = count_of_songs
    return music


#создаю словари под разные альбомы
album_1 = make_album('noize', 'последний альбом')
album_2 = make_album('валентин стрыкало', 'смирись и расслабься', 14)
album_3 = make_album(name_of_album='EP#3', name_of_singer='Электрофорез', count_of_songs=4)

#печатаю информацию об альбомах
print(album_1)
print(album_2)
print(album_3)