import sys
import time
import codecs
import json
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
GT_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'ground_truth')

from dige.extractor import faerie_extractor

class TestFaerieMethods(unittest.TestCase):
    def setUp(self):
        self.gt_filepath = os.path.join(GT_DATA_DIR, 'all_extractions_july_2016.jl')

    def tearDown(self):
        pass

    def test_faerie(self):
        ans = []
        with codecs.open(self.gt_filepath, 'r', 'utf-8') as file_handler:
            for line in file_handler.readlines():
                line = json.loads(line.strip())
                annotation = faerie_extractor.run4text(line['content'])
                annotation = faerie_extractor.clean_extraction(annotation)
                line.setdefault('annotated_names', annotation)
                ans.append(line)
        print ans

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestFaerieMethods('test_faerie'))
        
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



