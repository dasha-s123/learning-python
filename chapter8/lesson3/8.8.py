def make_album(name_of_singer, name_of_album, count_of_songs=None):
    """возвращает словарь с именем музыканта и названием альбома"""
    music = {"singer": name_of_singer.title(), "name": name_of_album}
    if count_of_songs:
        music["count_of_songs"] = count_of_songs
    return music


while True:
    print("Let's create new alnum!")
    print('(Enter "q" if you want to quit)\n')

    # задаю аргумент имени исполнителя
    singer = input("Enter singer name: ")
    if singer == 'q':
        break

    # задаю аргумент названия альбома
    name = input("Enter name of album: ")
    if name == 'q':
        break

    # задаю параметр с возможностью его отсутствия (количество песен в альбоме)
    print("\t(Write '-' if you don't know the following parameter)")
    count_of_songs = input("Enter count of sons: ")
    if count_of_songs == 'q':
        break
    if count_of_songs == '-':
        count_of_songs = None

    #создаю альбом вывожу информацию о нем
    album = make_album(singer.title(), name, count_of_songs)#
    print("\nInformation about your album:")
    print(album)
    print()