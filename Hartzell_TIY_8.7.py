def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if number_of_songs is not None:
        album['number_of_songs'] = number_of_songs
    return album

# Creating album dictionaries
album_1 = make_album('Led Zeppelin', 2)
album_2 = make_album('Nazareth', 'Hair of the Dog')
album_3 = make_album('Led Zeppelin', 'Mothership')

# Print
print(album_1)
print(album_2)
print(album_3)