# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 18:56:39
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 19:41:57

import os
import sys
import codecs
import json
import faerie

FAERIE_CONF_DIR = os.path.join(os.path.dirname(__file__), 'conf')

dictionary_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_dictionary.json'))
# documents_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_documents.json'))
# config_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_config.json'))

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import dict_loader

def generate_dictionary(items):
    dictionary = []
    for item in items:
        item = item.lower()
        dictionary.append({'content': item, 'id': item})
    with codecs.open(dictionary_, 'w', 'utf-8') as file_handler:
        for item in dictionary:
            file_handler.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    path = os.path.join(dict_loader.DICT_PATH, 'person_name')
    items = dict_loader.load_dictionary_dir(path)
    generate_dictionary(items)
