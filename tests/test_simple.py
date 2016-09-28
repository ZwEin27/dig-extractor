import sys
import time
import codecs
import json
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
GT_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'ground_truth')

from dige.extractor import simple_extractor

class TestSimpleMethods(unittest.TestCase):
    def setUp(self):
        self.gt_filepath_sampled = os.path.join(GT_DATA_DIR, 'all_extractions_july_2016_50.jl')
        self.gt_filepath_annotated = os.path.join(GT_DATA_DIR, 'all_extractions_july_2016_50_annotated.jl')

    def tearDown(self):
        pass

    def test_simple(self):
        ans = []
        report = []
        with codecs.open(self.gt_filepath_sampled, 'r', 'utf-8') as file_handler:
            for line in file_handler.readlines():
                line = json.loads(line.strip().lower())
                
                annotation = simple_extractor.run4text(line['content'])
                if annotation:
                    line.setdefault('annotated_names', annotation)
                    ans.append(line)

                correct_names = line['correct_names']

                count = 0
                for anno in annotation:
                    if anno in correct_names:
                        count += 1
                report.append(count)
                break

        # 33/50
        print len([_ for _ in report if _]), 'out of', len(report), 'extracted'

        # ans = [_ for _ in ans if _['annotated_names']]
        # print json.dumps(ans, indent=4)

        with codecs.open(self.gt_filepath_annotated, 'w', 'utf-8') as file_handler:
            for item in ans:
                file_handler.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestSimpleMethods('test_simple'))
        
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



