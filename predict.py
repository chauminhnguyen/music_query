import os
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import pickle
from annoy import AnnoyIndex
from pydub import AudioSegment
import pydub
from collections import Counter
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
f=100
u = AnnoyIndex(f,metric='angular')
u.load('music.ann')
file = open('time.pk', 'rb')
file1 = open('songs.pk','rb') 
# dump information to that file
time = pickle.load(file)
songs = pickle.load(file1)

data_sir= 'E:/Computer Science/HK5/CS336/Project/data/mp3/'
data_dir1='E:/Computer Science/HK5/CS336/Project/app/'
k ='Di-Theo-Bong-Mat-Troi-Den-Giang-Nguyen (mp3cut.net).mp3'
song1 = os.path.join(data_dir1,k)
sound = AudioSegment.from_file(song1, format="mp3").set_frame_rate(16000)
song = k.split(".mp3")[0]
song = os.path.join(data_dir1,song+".wav")
sound.export(song, format="wav")  
y,sr= librosa.load(song,sr= 16000)
feat = extract_features(y)
results = []
count_s_begin = []
for i in range(0,feat.shape[0]-10,5):
  crop_feat = crop_feature(feat,i,nb_step=10)
  result = u.get_nns_by_vector(crop_feat,n=1)
  count_s_begin.append(result[0])
  result_songs = [songs[k] for k in result]
  results.append(result_songs)
results= np.array(results).flatten()
most_song = Counter(results)
arr = (most_song.most_common())[0][0]
print(arr)
result_song = arr.split("E:/Computer Science/HK5/CS336/Project/data/wav/")[1]
print(result_song)
list_song = os.listdir("E:/Computer Science/HK5/CS336/Project/data/wav")
index_song = list_song.index(result_song)
print("Doan nhac bat dau tu giay thu:", (int(count_s_begin[0])-int(time[index_song]))*0.1)
print("Ket thuc o giay thu:", (int(count_s_begin[0])-int(time[index_song]))*0.1+ (len(y)/16000))
