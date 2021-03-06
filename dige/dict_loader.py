# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 14:55:45
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-28 14:00:16

import os
import sys
import json
import codecs

DICT_PATH = os.path.join(os.path.dirname(__file__), '..', 'dictionaries')

def load_dictionary_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as file_handler:
        return [_.strip().lower() for _ in file_handler.readlines()]

def load_dictionary_dir(dirpath):
    ans = []
    for filename in os.listdir(dirpath):
        if filename[0] == '.':
            continue
        if filename.split('.')[-1] != 'txt':
            continue
        path = os.path.join(dirpath, filename)
        ans += load_dictionary_file(path)
    ans = list(set(ans))
    return ans


if __name__ == '__main__':

    # # load file
    # path = os.path.join(DICT_PATH, 'person_name', 'female_irish.txt')
    # print load_dictionary_file(path)


    # load dir
    # path = os.path.join(DICT_PATH, 'person_name')
    # print load_dictionary_dir(path)

    set1 = set(load_dictionary_file(os.path.join(DICT_PATH, 'name.test')))
    set2 = set(load_dictionary_dir(os.path.join(DICT_PATH, 'person_name')))
    
    # intersection
    # for tmp in set1.intersection(set2):
    #     print str(tmp)

    # reverse
    for tmp in set1:
        if tmp not in set2:
            print str(tmp.encode('utf-8'))

