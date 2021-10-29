import unittest
from climatepredictor import max_time

class MaxRangeTest(unittest.TestCase):
    '''
    Tests the max range function
    '''
    def test_max_range(self):
        default = 'default'
        max = max_time(10,1,1)
        self.assertEqual(max, 9)
        max = max_time(10,1,-1)
        self.assertEqual(max, 1)


if __name__ == '__main__':
    unittest.main()