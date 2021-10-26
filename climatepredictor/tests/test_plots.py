import unittest
import matplotlib.pyplot as plt
from unittest.mock import patch
from climatepredictor import plotting, solve_over_time

class PlotTest(unittest.TestCase):
    '''
    Test the plotting function
    '''
    def test_plotting_yerror(self):
        solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
        
        with self.assertRaises(ValueError):
            plot = plotting(solution, 'Off','Off','Off','co2')

        with self.assertRaises(ValueError):
            plot = plotting(solution, 'Off','Off','Off','cloud cover')
        
        with self.assertRaises(ValueError):
            plot = plotting(solution, 'Off','Off','Off','time')

    def test_plotting_xerror(self):
        solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)

        with self.assertRaises(ValueError):
            plot = plotting(solution, 'On', 'On', 'On', None)

    # @patch('matplotlib.pyplot.show')
    # def test_plotting_called(self,mock_pyplot):
    #     solution = solve_over_time(1368,0.3,0.5,0.5,5.67e-8,1,50,0,0,0,0,10)
    #     plotting(solution,'On','On','On','co2')
    #     #mock_pyplot.show.assert_called_once()
    #     assert mock_pyplot.show.called

if __name__ == '__main__':
    unittest.main()