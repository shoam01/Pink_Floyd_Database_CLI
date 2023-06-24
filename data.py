FILE_PATH = "Pink_Floyd_DB.txt"

ALBUM_SEP = "#"
ATTR_SEP = "::"
SONG_SEP = "*"
LIST_SEP = ", "

NAME = 0
CUR_SONG_LEN = 2
CUR_SONG_LYRICS = 3

OFFSET = 1

SONG_LEN = 0
SONG_LYRICS = 1

SPACE = " "
NOTHING = ""

QUIT = "Goodbye!"


def parse_db() :
    """

    return:
    """
    with open(FILE_PATH, "r") as file :
        file_text = file.read()

    albums = dict()
    songs = dict()

    file_text = file_text.split(ALBUM_SEP)

    for album in file_text[OFFSET :] :
        album_name = albums[album.split(ATTR_SEP)[NAME]] = []

        for song in album.split(SONG_SEP)[OFFSET :] :
            song_attrs = song.split(ATTR_SEP)
            song_name = song_attrs[NAME]

            album_name.append(song_name)

            songs[song_name] = (song_attrs[CUR_SONG_LEN], song_attrs[CUR_SONG_LYRICS])

    return songs, albums


def get_albums(songs, albums, temp) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param temp: Temporary data parameter
    """

    return LIST_SEP.join(albums.keys())


def get_album_songs(songs, albums, album) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param album: A given album
    """
    return LIST_SEP.join(albums[album])


def get_song_len(songs, albums, song) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param song: A given song
    """
    return songs[song][SONG_LEN]


def get_song_lyrics(songs, albums, song) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param song: A given song
    """
    return songs[song][SONG_LYRICS]


def get_album_of_song(songs, albums, song) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param song: A given song
    """
    for album in albums.keys() :
        if song in albums[album] :
            return album

    return SPACE


def get_song_by_name(songs, albums, name) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param name: A given song's name
    """
    matching_songs = LIST_SEP.join([song_name for song_name in songs.keys() if name in song_name])

    if matching_songs == NOTHING :
        return SPACE

    return matching_songs


def get_song_by_lyric(songs, albums, lyric) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param lyric: A given lyric
    """

    matching_songs = LIST_SEP.join([song_name for song_name in songs.keys() if lyric in songs[song_name][SONG_LYRICS]])

    if matching_songs == NOTHING :
        return SPACE

    return matching_songs


def quit(songs, albums, temp) :
    """

    :param songs: Dict of songs and their attributes from the Pink Floyd database
    :param albums: Dict of albums and their songs from the Pink Floyd database
    :param temp: Temporary data parameter
    """
    return QUIT


OPTIONS = {"1" : get_albums,
           "2" : get_album_songs,
           "3" : get_song_len,
           "4" : get_song_lyrics,
           "5" : get_album_of_song,
           "6" : get_song_by_name,
           "7" : get_song_by_lyric,
           "8" : quit}