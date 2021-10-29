import unittest
import matplotlib.pyplot as plt
from unittest.mock import patch
from climatepredictor import make_plot, solve_over_time

class PlotTest(unittest.TestCase):
    '''
    Test the plotting function
    '''
    def test_plotting_yerror(self):
        solution, t = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
        
        with self.assertRaises(ValueError):
            plot = make_plot(solution, t, 'Off','Off','Off','time',0,0,0,0,0,0,0,0)

    def test_plotting_xerror(self):
        solution, t = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)

        with self.assertRaises(ValueError):
            plot = make_plot(solution, t, 'On', 'On', 'On', None,0,0,0,0,0,0,0,0)

if __name__ == '__main__':
    unittest.main()