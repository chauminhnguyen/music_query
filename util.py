# <<<<<<< HEAD
import os
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import pickle
from annoy import AnnoyIndex
import model
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


def predict(feat,songs,model):
    results = []
    count_s_begin = []
    for i in range(0,feat.shape[0]-10,5):
        crop_feat = crop_feature(feat,i,nb_step=10)
        if len(count_s_begin)==0:
            count_s_begin = crop_feat
        result = model.get_nns_by_vector(crop_feat,n=5)
        result_songs = [songs[k] for k in result]
        results.append(result_songs)
    results= np.array(results).flatten()
    most_song = Counter(results)
    arr = most_song.most_common()
    return arr,count_s_begin
# =======
import os
import glob
import librosa
from tqdm import tqdm
import numpy as np
from python_speech_features import mfcc, fbank, logfbank
import pickle
from annoy import AnnoyIndex
import model
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


def predict(feat,songs,model):
    results = []
    count_s_begin = []
    for i in range(0,feat.shape[0]-10,5):
        crop_feat = crop_feature(feat,i,nb_step=10)
        if len(count_s_begin)==0:
            count_s_begin = crop_feat
        result = model.get_nns_by_vector(crop_feat,n=5)
        result_songs = [songs[k] for k in result]
        results.append(result_songs)
    results= np.array(results).flatten()
    most_song = Counter(results)
    arr = most_song.most_common()
    return arr,count_s_begin
# >>>>>>> 30452720899e092f6c2e7549dced3856cb750459
