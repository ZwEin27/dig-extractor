# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 15:21:54
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 19:37:10


import faerie
import os
import json
import codecs

FAERIE_CONF_DIR = os.path.join(os.path.dirname(__file__), 'conf')

dictionary_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_dictionary.json'))
documents_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_documents.json'))
config_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'dige_config.json'))

faerie_config = json.loads(open(config_).read())
faerie_dictionary = faerie.readDict(dictionary_, faerie_config)

def clean_extraction(json_obj):
    if not json_obj:
        return None
    if 'entities' not in json_obj:
        return None
    json_obj = json_obj['entities']
    return json_obj.keys()

def run4text(content):
    jsonline = {'content': content, 'id': 'single'}
    jsonline = faerie.processDoc(jsonline, faerie_dictionary, faerie_config)
    return jsonline

def run4path(path):
    with codecs.open(path, 'r', 'utf-8') as file_handler:
        for line in file_handler.readlines():
            extraction = run4text(line.strip())
            extraction = clean_extraction(extraction)
            yield extraction

if __name__ == '__main__':
    print run4path(documents_)
