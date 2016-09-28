# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-25 15:21:54
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-28 14:06:12


import faerie
import os
import json
import codecs

def run4text(content):
    

    return jsonline

def run4path(path):
    with codecs.open(path, 'r', 'utf-8') as file_handler:
        for line in file_handler.readlines():
            extraction = run4text(line.strip())
            yield extraction

if __name__ == '__main__':
    print run4path(documents_)
