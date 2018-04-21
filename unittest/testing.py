import unittest
from to_be_tested import *

class TestSomeFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.classbegin = True

    @classmethod
    def tearDownClass(self):
        self.classbegin = False

    def setUp(self):
        # print("setup")
        self.begin = True
    
    def tearDown(self):
        # print("teardown")
        self.begin = False

    def test_add(self):
        self.assertEqual(add(1,2), 3)
    
    def test_mult(self):
        self.assertEqual(mult(2,3), 6)
    
    def test_setup(self):
        # print(self.begin)
        self.assertEqual(self.begin, True)

    def test_setupclass(self):
        self.assertEqual(self.classbegin, True)

if __name__ == '__main__':
    unittest.main()   