import os
import csv
from functools import reduce


def create_csv(words):
    with open('songs-info-file.csv', 'w', newline='', encoding='utf-8-sig') as indexFile:

        # declaring the fieldnames for the CSV file
        fieldNames = ['song', 'artists']

        # creating a DictWriter object
        csvWriter = csv.DictWriter(indexFile, fieldnames=fieldNames)

        # writing the header
        csvWriter.writeheader()

        for word, fileDetails in words.items():
            # writing the row
            csvWriter.writerow(
                {'song': word, 'artists': fileDetails})


def get_songs_info_dict(songs_lst):
    songs_info = {}
    for song_title in songs_lst:
        song_name = song_title.split(' - ')[0]
        artists_name = song_title.split(' - ')[-1].split('.')[0]
        songs_info[song_name] = artists_name
    return songs_info


def main(songs_path):
    songs_lst = os.listdir(songs_path)
    songs_info = get_songs_info_dict(songs_lst)
    create_csv(songs_info)


if __name__ == "__main__":
    songs_path = './data/lyrics/'
    main(songs_path)
