# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 14:55:45
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 15:13:21

import os
import sys
import json
import codecs
import faerie

DICT_PATH = os.path.join(os.path.dirname(__file__), '..', 'dictionaries')


def load_dictionary(path):
    with codecs.open(path, 'r', 'utf-8') as file_handler:
        return [_.strip() for _ in file_handler.readlines()]

    # return json.load()

if __name__ == '__main__':

    path = os.path.join(DICT_PATH, 'person_name', 'female_irish.txt')
    print load_dictionary(path)


