def main(song_kw, song_db):
    results = []
    for song_name in song_db:
        song_name = song_name.split(' ')
        if song_kw in song_name:
            results.append(song_name)
    return results
