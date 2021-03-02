# -*- coding: utf-8 -*-

import string
import os
import csv
from functools import reduce
import time

# TODO - decrease for loops used somehow
# TODO - try applying map and reduce


def createDictionary(directory):
    wordsAdded = {}
    # getting the files in the directory
    fileList = os.listdir(directory)

    for file in fileList:
        with open(directory + file, 'r', encoding='utf-8') as f:
            # getting all the words in the file in lowercase
            # also, getting rid of any trailing punctuation
            # removing repetitions of a word in the file
            words = set(map(
                lambda x: x[:-1] if x[-1] in [',', '!', '?', '.'] else x, f.read().lower().split()))

            table = str.maketrans('', '', string.punctuation)
            for word in words:
                # clean word
                word = word.translate(table)

                # checking whether the current word is new or not
                if word not in wordsAdded.keys():
                    # if new, creating a new entry for the word in the dictionary
                    wordsAdded[word] = {}
                    wordsAdded[word]['songsNames'] = []
                # adding the file and its path to the dictionary
                wordsAdded[word]['songsNames'] += [f.name]
    return wordsAdded


def writeToFile(words):
    with open('./utils/index-file.csv', 'w', newline='', encoding='utf-8-sig') as indexFile:

        # declaring the fieldnames for the CSV file
        fieldNames = ['word', 'songsNames']

        # creating a DictWriter object
        csvWriter = csv.DictWriter(indexFile, fieldnames=fieldNames)

        # writing the header
        # csvWriter.writeheader()

        for word, fileDetails in words.items():
            # creating a string of all the file names and file paths
            fileNameString = reduce(
                lambda x, y: x + ", " + y, fileDetails['songsNames'])

            # writing the row
            csvWriter.writerow(
                {'word': word, 'songsNames': fileNameString})


def main():
    start = time.process_time()
    directory = './data/lyrics/'
    writeToFile(createDictionary(directory))
    print("Finished")
    print(time.process_time() - start)


if __name__ == '__main__':
    main()
