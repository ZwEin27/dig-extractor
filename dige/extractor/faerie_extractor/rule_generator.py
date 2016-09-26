# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 18:56:39
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 19:34:01

import os
import sys
import codecs
import json
import faerie

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import dict_loader



if __name__ == '__main__':
    path = os.path.join(dict_loader.DICT_PATH, 'person_name')
    print dict_loader.load_dictionary_dir(path)
