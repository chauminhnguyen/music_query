from annoy import AnnoyIndex
import os
import librosa
from tqdm import tqdm
from python_speech_features import mfcc, fbank, logfbank
import numpy as np
import pickle
from annoy import AnnoyIndex
import argparse

def extract_features(y, sr = 16000, nfilt= 10, winsteps=0.02):
    try:
        feat = mfcc(y, sr,nfilt=nfilt,winstep=winsteps)
        return feat
    except:
        raise Exception("Exception feature error")
def crop_feature(feat, i=0, nb_step=10, maxlen=100):
    crop_feat = np.array(feat[i:i+nb_step]).flatten()
    crop_feat = np.pad(crop_feat, (0,maxlen-len(crop_feat)), mode ="constant")
    return crop_feat

parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', help='path to music data mp3/wav')
args = parser.parse_args()

features=[]
songs=[]
time= []
list_song = os.listdir(args.data_dir)
for song in tqdm(os.listdir(args.data_dir)):
    song = os.path.join(args.data_dir,song) 
    y, sr = librosa.load(song, sr = 16000)
    feat = extract_features(y)
    for i in range(0, feat.shape[0]-10,5):
        features.append(crop_feature(feat, i , nb_step=10))
        if song not in songs:
            songs.append(song)
            time.append(len(songs)-1)
        else:
            songs.append(song)
pickle.dump(features,open('feature.pk','wb'))
pickle.dump(songs,open('songs.pk','wb'))
pickle.dump(time, open('time.pk','wb'))
pickle.dump(list_song, open('list_song.pk','wb'))
f =100
t = AnnoyIndex(f,metric='angular')
for i in range(len(features)):
  v = features[i]
  t.add_item(i,v)
t.build(100)
t.save('music.ann')