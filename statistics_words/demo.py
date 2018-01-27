#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 1/27/18 11:30 AM 
# @Author : Tony 
# @Site :  
# @File : demo.py 
# @Software: PyCharm

import string
from matplotlib import pyplot as plt

def process_line(line, wordcount):
    ''' processing every line '''
    line = line.replace('-', ' ')
    for word in line.split():
        # remove , ' '' etc.
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        # count the word by the founction of dictionary --> get()
        wordcount[word] = wordcount.get(word, 0) + 1


def process_file(filename):
    ''' process file '''

    wordcount = {}

    with open(filename, 'r') as f:
        for line in f:
            process_line(line, wordcount)

    return wordcount


def top_n(wordcount, num):
    ''' get top $num words'''

    word_list = []
    count_list = []
    ls = []
    for key, val in wordcount.items():
        ls.append((val, key))

    # sorted by reverse and then can get the top-N
    ls.sort(reverse=True)

    # Only pick out top-N
    for key, val in ls[:num]:
        word_list.append(val)
        count_list.append(key)

    return word_list,count_list


def run():
    ''' main function '''

    wordcount = process_file('This_Side_of_Paradise.txt')

    # get TOP-N
    word, count = top_n(wordcount, 5)
    # print(word,count)

    plt.bar(word, count)
    plt.xlabel('words')
    plt.ylabel('rate')
    plt.title('words count')
    plt.show()


if __name__ == '__main__':
    run()