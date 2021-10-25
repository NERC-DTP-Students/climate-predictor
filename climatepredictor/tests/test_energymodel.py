import unittest
import numpy as np
import climatepredictor
from climatepredictor import solve_model, solve_over_time

class ModelTest(unittest.TestCase):
    '''
    Tests the energy balance model
    '''
    def test_solve_model_shape(self):
        solution = solve_model(1368,0.3,0.5,0.5,5.67e-8)
        self.assertEqual(np.shape(solution), (3,1))

if __name__ == '__main__':
    unittest.main()