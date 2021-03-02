'''
output: list of songs names
'''
import string
import csv
import re
import numpy as np
import os


def idf(docs, total_docs):
    DF = len(docs)
    return 1 + np.log(len(total_docs) / DF)


table = str.maketrans('', '', string.punctuation)


def calc_TF_IDF(vocab, mydict, content):
    for word in vocab:
        for doc in mydict[word]:
            pass


def tf_idf(mydict, total_docs):
    terms = mydict.keys()
    TF = np.zeros((len(terms), len(total_docs)))
    IDF = []
    for i, term in enumerate(terms):
        for doc in mydict[term]:
            song_name = doc.split('/')[-1]
            j = total_docs.index(song_name)
            doc = open(doc, 'r', encoding='utf-8').read()

            words = list(map(
                lambda x: x[:-1] if x[-1] in [',', '!', '?', '.'] else x, doc.lower().split()))
            doc = [w.translate(table) for w in words]
            TF[i, j] = doc.count(term)
        IDF.append(idf(mydict[term], total_docs))

    IDF = np.array([IDF]).T
    TF = TF / np.sum(TF, axis=0)
    return TF * IDF


def qtf_idf(mydict, query):
    terms = mydict.keys()
    TF = np.zeros((len(terms), 1))
    for i, term in enumerate(terms):
        # for j, word in enumerate(query):
        TF[i] = query.count(term)
    IDF = idf(mydict[term], query)
    TF = TF / np.sum(TF, axis=0)
    return TF * IDF


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
    words = list(map(
        lambda x: x[:-1] if x[-1] in [',', '!', '?', '.'] else x, query.lower().split()))

    # stop words
    # words = query.split()

    table = str.maketrans('', '', string.punctuation)
    query = [w.translate(table) for w in words]

    # rankings
    # mydict.pop('\ufeffin')
    total_docs = os.listdir('./data/lyrics')
    TF_IDF = tf_idf(mydict, total_docs)
    qTF_IDF = qtf_idf(mydict, query)

    dists = np.linalg.norm(TF_IDF - qTF_IDF, axis=0)
    rank = np.argsort(dists)
    topK = 10
    res = []
    for i in range(topK):
        res.append(total_docs[rank[i]])
    return res

