# <<<<<<< HEAD

# import pickle
# from annoy import AnnoyIndex

# def load_model():
    # f=100
    # u = AnnoyIndex(f,metric='angular')
    # u.load('music.ann')
    # file = open('time.pk', 'rb')
    # file1 = open('songs.pk','rb')
    # file2 = open('list_song.pk','rb')
    # dump information to that file
    # time = pickle.load(file)
    # songs = pickle.load(file1)
    # list_song = pickle.load(file2)
# =======

import pickle
from annoy import AnnoyIndex

def load_model():
    f=100
    u = AnnoyIndex(f,metric='angular')
    u.load('music.ann')
    file = open('time.pk', 'rb')
    file1 = open('songs.pk','rb')
    file2 = open('list_song.pk','rb')
    # dump information to that file
    time = pickle.load(file)
    songs = pickle.load(file1)
    list_song = pickle.load(file2)
# >>>>>>> 30452720899e092f6c2e7549dced3856cb750459
    return u, time, songs,list_song