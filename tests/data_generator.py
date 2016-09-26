# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-16 15:20:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-25 19:12:27

import os
import sys
import csv
import json
from random import shuffle

def gt_template_generator(input_path, output_path=None, sample_num=None, sample_rate=None):
    dataset = []
    with open(input_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            label =row[0]
            content = row[1].decode('utf-8', 'ignore').encode('ascii', 'ignore')
            dataset.append(content)

    shuffle(dataset)

    size = len(dataset)
    if sample_num and sample_num <= size:
        dataset = dataset[:sample_num]
    elif sample_rate and sample_rate * size <= size:
        sample_num = int(sample_rate * size)
        dataset = dataset[:sample_num]

    dataset = [{'content':data, 'correct_names': []} for data in dataset]

    if output_path:
        with open(output_path, 'wb') as file_handler:
            for data in dataset:
                file_handler.write(json.dumps(data, indent=4) + '\n')



if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'data', 'all_extractions_july_2016.csv')
    output_path = os.path.join(os.path.dirname(__file__), 'data', 'ground_truth.json')
    gt_template_generator(input_path, output_path=output_path, sample_num=50)
