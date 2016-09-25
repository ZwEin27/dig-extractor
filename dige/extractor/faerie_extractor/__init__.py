# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 15:21:54
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 15:44:25


import faerie
import os
import json
import codecs

FAERIE_CONF_DIR = os.path.join(os.path.dirname(__file__), 'conf')

dictionary_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_dictionary.json'))
documents_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_documents.json'))
config_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_config.json'))

faerie_config = json.loads(open(config_).read())
faerie_dictionary = faerie.readDict(dictionary_, faerie_config)

def run4text(content):
    jsonline = {'content': content, 'id': 'single'}
    jsonline = faerie.processDoc(jsonline, faerie_dictionary, faerie_config)
    return jsonline

def run4path(path):
    with codecs.open(path, 'r', 'utf-8') as file_handler:
        for line in file_handler.readlines():
            print run4text(line.strip())


if __name__ == '__main__':
    run4path(documents_)
