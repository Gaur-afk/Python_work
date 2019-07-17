def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('Eminem', 'Kamikaze')
print(album)

album = make_album('post malone', 'beerbongs and bentleys', 9)
print(album)

album = make_album('21 savage', 'issa album')
print(album)