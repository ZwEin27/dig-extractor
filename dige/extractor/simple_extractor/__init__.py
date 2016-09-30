# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 15:21:54
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-28 14:12:09


import faerie
import os
import json
import codecs
from nltk.tokenize import word_tokenize

def run4text(content, dictionary):

    ans = []
    tokens = word_tokenize(content)
    for token in tokens:
        if token.lower() in dictionary:
            ans.append(token)
    return ans

def run4path(path, dictionary):
    extraction = []
    with codecs.open(path, 'r', 'utf-8') as file_handler:
        for line in file_handler.readlines():
            extraction += run4text(line.strip(), dictionary)
    return extraction
    
if __name__ == '__main__':
    print run4path(documents_)
