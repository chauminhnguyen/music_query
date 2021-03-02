import glob
import numpy as np
import re


def load_data_in_a_directory(data_path):
    file_paths = glob.glob(data_path)
    lst_contents = []
    for file_path in file_paths:
        words = file_path.split('\\')[-1].split(' - ')[0].replace('"', '').replace(
            '.', '').replace("'", "").lower().split()
        #words = set(words)
        lst_contents.append(words)
    return (lst_contents, file_paths)

# Doc noi dung cua tung file txt
# va xay dung tap "dictionary" chua danh sach cac tu


def build_dictionary(contents):
    dictionary = set()
    for content in contents:
        dictionary.update(content)
    return dictionary


def calc_tf_weighting(vocab, contents):
    TF = np.zeros((len(vocab), len(contents)))
    for i, word in enumerate(vocab):
        for j, content in enumerate(contents):
            TF[i, j] = content.count(word)
    # Chuan hoa
    TF = TF / np.sum(TF, axis=0)
    return TF
# MAIN


def main(query):
    contents, paths = load_data_in_a_directory('./data/lyrics/*.txt')
    vocab = build_dictionary(contents)

    TF = calc_tf_weighting(vocab, contents)
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    DF = np.sum(TF != 0, axis=1)
    IDF = 1 + np.log(len(contents) / DF)
    IDF = np.array([IDF]).T

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF

    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    rank = np.argsort(dists)
    topK = 5
    res = []
    for i in range(topK):
        res.append(paths[rank[i]].split('\\')[-1].split('.')[0])
    return res


