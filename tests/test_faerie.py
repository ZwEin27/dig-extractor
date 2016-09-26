import sys
import time
import codecs
import json
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
GT_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'ground_truth')

class TestFaerieMethods(unittest.TestCase):
    def setUp(self):
        self.gt_filepath = os.path.join(GT_DATA_DIR, 'all_extractions_july_2016.jl')

    def tearDown(self):
        pass

    def test_faerie(self):
        with codecs.open(path, 'r', 'utf-8') as file_handler:
            for line in file_handler.readlines():
                line = json.loads(line.strip())
                line['content']
    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestCSVMethods('test_faerie'))
        
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



