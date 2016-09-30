# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-14 13:56:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-29 22:05:37

import os
import sys
import csv
import json
import codecs
import yaml

def generate_data_csv(dataset, path, default_label=-1):
    if not dataset:
        return
    with open(path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['label', 'extracted_text'])
        writer.writeheader()
        for data in dataset:
            try:
                content = data
                if not content:
                    continue
                content = content.replace('\n', ' ').replace('\r', ' ')
                content = unicode(content, errors='ignore')

                data = {}
                data.setdefault('label', default_label)
                data.setdefault('extracted_text', content)

                writer.writerow(data)
            except Exception as e:
                print e
                raise Exception('generate_data_csv')


def gt_template_generator(dataset, output_path=None):

    dataset = [{'content': content, 'correct_names': [], 'annotated': spec} for (content, spec) in dataset]

    if output_path:
        with open(output_path, 'wb') as file_handler:
            for data in dataset:
                file_handler.write(json.dumps(data) + '\n')

def load_jsonlines(intput_path, output_path=None):
    dataset = []
    i = 0

    for line in codecs.open(intput_path, 'r'):
        try:
            json_obj = yaml.safe_load(line)
        except Exception as e:
            # print e, i
            # print line.strip()
            continue
        i += 1

        # phone = json_obj['telephone'] if 'telephone' in json_obj else None
        # location = json_obj['addressLocality'] if 'addressLocality' in json_obj else None
        age = json_obj['age'] if 'age' in json_obj else None
        # gender = json_obj['gender'] if 'gender' in json_obj else None
        # url = json_obj['url'] if 'url' in json_obj else None
        readability_text = json_obj['readability_text'] if 'readability_text' in json_obj else None
 
        node_text = readability_text if readability_text else ' '

        if not isinstance(node_text, basestring):
            try:
                node_text = ' '.join([_ for _ in node_text if _ and isinstance(_, basestring)])
            except:
                node_text = str(node_text)
        node_text = node_text.encode('ascii', 'ignore')
        dataset.append((node_text, age))
        break

    gt_template_generator(dataset, output_path=output_path)

    return dataset


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'data', 'all_extractions_july_2016.jl')
    output_path = os.path.join(os.path.dirname(__file__), 'data', 'all_extractions_july_2016_specific.csv')
    load_jsonlines(input_path, output_path=output_path)
