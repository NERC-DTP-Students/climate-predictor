import unittest
from climatepredictor import plotting, solve_over_time

class PlotTest(unittest.TestCase):
    '''
    Test the plotting function
    '''
    def test_plotting(self):
        solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
        with self.assertRaises(ValueError):
            plot = plotting(solution, 'On','On','On','Off','Off','Off')

if __name__ == '__main__':
    unittest.main()