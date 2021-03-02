def main(artist_kw, artist_db):
    results = []
    for artist_names in artist_db:
        artist_names = artist_names.split('_')
        for artist_name in artist_names:
            artist_name = artist_name.split(' ')
            if artist_kw in artist_name:
                results.append(artist_name)
    return results
