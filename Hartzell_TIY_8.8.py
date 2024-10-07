def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if number_of_songs is not None:
        album['number_of_songs'] = number_of_songs
    return album

# While loop
while True:
    print("\nEnter the album details (or 'q' to quit):")

    artist = input("Artist: ")
    if artist.lower() == 'q':
        break

    title = input("Title: ")
    if title.lower() == 'q':
        break

    album = make_album(artist, title)
    print("Album created:", album)

print("Thank you for using the album creator!")