import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

class TestCSVMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dige(self):
        pass

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestCSVMethods("test_dige"))
        
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



