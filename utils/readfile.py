import re

def lyric(path, query):
    song_name = "./data/lyrics/"+ path
    with open(song_name, 'r', encoding='utf-8') as f:
        # song_lyric = f.read()
        # result = []
        # result.append(song_name.split('/')[-1].split('.')[0])
        index_arr = [0]
        lyric = []
        query = query.split(" ")
        with open(song_name, 'r', encoding='utf-8') as f:
            song_lyric = f.read()
            for word in query:
                indexes = re.finditer("\\b(?i)" + word + "\\b", song_lyric)
                for index in indexes:
                    if index_arr[-1] == index.start(0) + 1:
                        index_arr[-1] = index.end(0)
                    else:
                        index_arr.append(index.start(0))
                        index_arr.append(index.end(0))
        index_arr.append(len(song_lyric))
        index_arr = sorted(index_arr)
        for i in range(len(index_arr)-1):
            temp = song_lyric[index_arr[i]:index_arr[i+1]]
            temp = temp.replace('\n', '<br>')
            lyric.append(temp)
        lyric.append(song_lyric[index_arr[len(index_arr)-1]:])
        # result.append(lyric)
    return lyric

