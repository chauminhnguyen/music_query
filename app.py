# <<<<<<< HEAD


from flask import Flask, render_template, request, redirect,url_for
import speech_recognition as sr
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
import io
import model
import util
from collections import Counter
import statistics 
from statistics import mode 
import utils.tf_idf_lyrics as tf_idf_lyrics
import utils.tf_idf_songs as tf_idf_songs
import utils.readfile as rd
app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template('index.html' )
@app.route("/queryaudio", methods=["GET", "POST"])
def queryaudio():
    result_song =''
    begin = 0
    end =0
    artists = []
    song_artist=[]
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        # file1 =file.filename.replace(".mp3",".wav")
        # sound = AudioSegment.from_mp3(file.filename)
        # sound.export(file1, format="wav")
        if file.filename == "":
            return redirect(request.url)

        if file:
            
            def first_feature(feat,index_song,temp,u):
                l=[]
                for i in range(int(temp[index_song]),int(temp[index_song+1]),1):
                    l.append((u.get_item_vector(i)))
                z = AnnoyIndex(100,metric='angular')
                for i in range(len(l)):
                    v = l[i]
                    z.add_item(i,v)
                z.build(100)
                x=[]
                for i in range(0,int(feat.shape[0]/50),1):
                    crop_feat = util.crop_feature(feat,i,nb_step=10)
                    result1 = z.get_nns_by_vector(crop_feat,n=1)
                    x.append(result1[0])
                return x
            def most_common(List): 
                return(mode(List)) 
            def begin_second(count_s_begin):
                count=0
                for i in range(0,len(count_s_begin),5):
                    k = count_s_begin[i:i+5]
                    try:
                        kq = (most_common(k)-count)
                        return kq
                    except:
                        pass
                    count+=1
            ef,sr= librosa.load(file.filename,sr= 16000)
            exact_feature = util.extract_features(ef)
            results,count_s_begin = util.predict(exact_feature, songs,model1)  
            result_song = []
            
            top = 5 
            for q in range(top):
                k = results[q][0]
                song = k.split("E:/Computer Science/HK5/CS336/Audio_query/data/")[1]
                song_artist.append(song)
                s_a = song.split(" -")
                artists.append(s_a[1].split(".mp3")[0])
                result_song.append(s_a[0])
            index_song = list_song.index(result_song[0] +" -" + artists[0]+".mp3")
            second_begin = first_feature(exact_feature,index_song,time,model1) 
            begin = begin_second(second_begin)
            begin = int(begin)*0.1
            end = begin + (len(ef)/16000)
    return render_template("queryaudio.html", songs = result_song,song_artist=song_artist, artists= artists, begin =begin, end =round(end,1))
results_temp1 = []
result_song_temp1 =[]
lyric_temp1 =[]
@app.route("/searchsong/<int:id>", methods=["GET", "POST"])
def searchsong(id):
    global results_temp1
    global result_song_temp1
    global lyric_temp1
    if request.method == "POST":
        query = request.form["inp"]
        results = tf_idf_songs.main(query)
        top = 5
        song_artist = []
        result_song = []
        lyrics = []
        for q in range(top):
            k = results[q]
            song = k.split(".txt")[0]
            song1 = song.split(" - ")[0]
            song_artist.append(song)
            results_temp1 = song_artist
            result_song.append(song1)
            result_song_temp1 = result_song
            lyrics.append(rd.lyric(k+".txt", query))
            lyric_temp1 = lyrics
        return render_template("searchsong.html", results=song_artist,result_song=result_song,lyrics=lyrics,index=0)
    else:
        return render_template("searchsong.html", results=results_temp1, result_song = result_song_temp1, lyrics= lyric_temp1,index=id)
results_temp = []
result_song_temp =[]
lyric_temp =[]
@app.route("/searchlyric/<int:id>", methods=["GET", "POST"])
def searchlyric(id):
    global results_temp
    global result_song_temp
    global lyric_temp 
    if request.method == "POST":
        query = request.form["inp"]
        results = tf_idf_lyrics.main(query)
        top = 5
        song_artist = []
        result_song = []
        lyrics = []
        for q in range(top):
            k = results[q]
            song = k.split(".txt")[0]
            song1 = song.split(" - ")[0]
            song_artist.append(song)
            results_temp = song_artist
            result_song.append(song1)
            result_song_temp = result_song
            lyrics.append(rd.lyric(k, query))
            lyric_temp = lyrics
        return render_template("searchlyric.html", results=song_artist,result_song=result_song,lyrics=lyrics,index=0)
    else:
        return render_template("searchlyric.html", results=results_temp, result_song = result_song_temp, lyrics= lyric_temp,index=id)
            
if __name__ == "__main__":
    model1, time,songs,list_song= model.load_model()
# =======


from flask import Flask, render_template, request, redirect,url_for
import speech_recognition as sr
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
import io
import model
import util
from collections import Counter
import statistics 
from statistics import mode 
import utils.tf_idf_lyrics as tf_idf_lyrics
import utils.tf_idf_songs as tf_idf_songs
import utils.readfile as rd
app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template('index.html' )
@app.route("/queryaudio", methods=["GET", "POST"])
def queryaudio():
    result_song =''
    begin = 0
    end =0
    artists = []
    song_artist=[]
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        # file1 =file.filename.replace(".mp3",".wav")
        # sound = AudioSegment.from_mp3(file.filename)
        # sound.export(file1, format="wav")
        if file.filename == "":
            return redirect(request.url)

        if file:
            
            def first_feature(feat,index_song,temp,u):
                l=[]
                for i in range(int(temp[index_song]),int(temp[index_song+1]),1):
                    l.append((u.get_item_vector(i)))
                z = AnnoyIndex(100,metric='angular')
                for i in range(len(l)):
                    v = l[i]
                    z.add_item(i,v)
                z.build(100)
                x=[]
                for i in range(0,int(feat.shape[0]/50),1):
                    crop_feat = util.crop_feature(feat,i,nb_step=10)
                    result1 = z.get_nns_by_vector(crop_feat,n=1)
                    x.append(result1[0])
                return x
            def most_common(List): 
                return(mode(List)) 
            def begin_second(count_s_begin):
                count=0
                for i in range(0,len(count_s_begin),5):
                    k = count_s_begin[i:i+5]
                    try:
                        kq = (most_common(k)-count)
                        return kq
                    except:
                        pass
                    count+=1
            ef,sr= librosa.load(file.filename,sr= 16000)
            exact_feature = util.extract_features(ef)
            results,count_s_begin = util.predict(exact_feature, songs,model1)  
            result_song = []
            
            top = 5 
            for q in range(top):
                k = results[q][0]
                song = k.split("E:/Computer Science/HK5/CS336/Audio_query/data/")[1]
                song_artist.append(song)
                s_a = song.split(" -")
                artists.append(s_a[1].split(".mp3")[0])
                result_song.append(s_a[0])
            index_song = list_song.index(result_song[0] +" -" + artists[0]+".mp3")
            second_begin = first_feature(exact_feature,index_song,time,model1) 
            begin = begin_second(second_begin)
            begin = int(begin)*0.1
            end = begin + (len(ef)/16000)
    return render_template("queryaudio.html", songs = result_song,song_artist=song_artist, artists= artists, begin =begin, end =round(end,1))
results_temp1 = []
result_song_temp1 =[]
lyric_temp1 =[]
@app.route("/searchsong/<int:id>", methods=["GET", "POST"])
def searchsong(id):
    global results_temp1
    global result_song_temp1
    global lyric_temp1
    if request.method == "POST":
        query = request.form["inp"]
        results = tf_idf_songs.main(query)
        top = 5
        song_artist = []
        result_song = []
        lyrics = []
        for q in range(top):
            k = results[q]
            song = k.split(".txt")[0]
            song1 = song.split(" - ")[0]
            song_artist.append(song)
            results_temp1 = song_artist
            result_song.append(song1)
            result_song_temp1 = result_song
            lyrics.append(rd.lyric(k+".txt", query))
            lyric_temp1 = lyrics
        return render_template("searchsong.html", results=song_artist,result_song=result_song,lyrics=lyrics,index=0)
    else:
        return render_template("searchsong.html", results=results_temp1, result_song = result_song_temp1, lyrics= lyric_temp1,index=id)
results_temp = []
result_song_temp =[]
lyric_temp =[]
@app.route("/searchlyric/<int:id>", methods=["GET", "POST"])
def searchlyric(id):
    global results_temp
    global result_song_temp
    global lyric_temp 
    if request.method == "POST":
        query = request.form["inp"]
        results = tf_idf_lyrics.main(query)
        top = 5
        song_artist = []
        result_song = []
        lyrics = []
        for q in range(top):
            k = results[q]
            song = k.split(".txt")[0]
            song1 = song.split(" - ")[0]
            song_artist.append(song)
            results_temp = song_artist
            result_song.append(song1)
            result_song_temp = result_song
            lyrics.append(rd.lyric(k, query))
            lyric_temp = lyrics
        return render_template("searchlyric.html", results=song_artist,result_song=result_song,lyrics=lyrics,index=0)
    else:
        return render_template("searchlyric.html", results=results_temp, result_song = result_song_temp, lyrics= lyric_temp,index=id)
            
if __name__ == "__main__":
    model1, time,songs,list_song= model.load_model()
# >>>>>>> 30452720899e092f6c2e7549dced3856cb750459
    app.run(debug=True, threaded=True)