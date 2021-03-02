import string
import csv
import re
import numpy as np


def ranking(songs_name):
    pass


def main(query):
    mydict = {}
    # read csv file to get {word : files path}
    with open('./utils/index-file.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            mydict[row[0]] = row[1].split(", ")

    # preprocess query
    # capital words
    # query = query.lower()
    words = set(map(
                lambda x: x[:-1] if x[-1] in [',', '!', '?', '.'] else x, query.lower().split()))

    # stop words
    # words = query.split()

    table = str.maketrans('', '', string.punctuation)
    query = [w.translate(table) for w in words]

    # start retrieval
    postings = []
    for word in query:
        try:
            postings.append(set(mydict[word]))
        except:
            continue

    if len(postings) == 0:
        return [None]

    songs_name = set.intersection(*postings)

    # rankings
    ranking(songs_name)

    results = []
    # get index of query in found songs
    for song_name in songs_name:
        result = []
        result.append(song_name.split('/')[-1].split('.')[0])
        index_arr = [0]
        lyric = []
        with open(song_name, 'r', encoding='utf-8') as f:
            song_lyric = f.read()
            for word in query:
                indexes = re.finditer("\\b(?i)" + word + "\\b", song_lyric)
                for index in indexes:
                    # print(index.start(0), index.end(0))
                    index_arr.append(index.start(0))
                    index_arr.append(index.end(0))
        index_arr.append(len(song_lyric))
        index_arr = sorted(index_arr)
        for i in range(len(index_arr)-1):
            temp = song_lyric[index_arr[i]:index_arr[i+1]]
            temp = temp.replace('\n', '<br>')
            lyric.append(temp)
        lyric.append(song_lyric[index_arr[len(index_arr)-1]:])
        result.append(lyric)
        results.append(result)
    return results
