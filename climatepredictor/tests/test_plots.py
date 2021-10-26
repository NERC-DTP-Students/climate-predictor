import unittest
from unittest.mock import patch
from climatepredictor import plotting, solve_over_time

class PlotTest(unittest.TestCase):
    '''
    Test the plotting function
    '''
    def test_plotting_error(self):
        solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
        with self.assertRaises(ValueError):
            plot = plotting(solution, 'Off','Off','Off','co2')

    # @patch('climatepredictor.plotting')
    # def test_plotting_called(self,mock_plt):
    #     solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
    #     plotting(solution,'On','On','On','co2')
    #     assert self.figure.called()

if __name__ == '__main__':
    unittest.main()