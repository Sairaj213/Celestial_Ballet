import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import numpy as np
from utils.math_utils import calculate_center_of_mass
from utils.visualization_tools import calculate_system_energy
from core.chaos_tools import perturb_initial_conditions

class TestDataIntegrityModule(unittest.TestCase):

    def setUp(self):

        class MockOdeResult:
            t: np.ndarray
            y: np.ndarray

        self.mock_result = MockOdeResult()
        n_points = 100
        self.mock_result.t = np.linspace(0, 10, n_points)
        self.mock_result.y = np.random.rand(18, n_points)
        
        self.mock_masses = [1.0, 1.0, 1.0]
        self.mock_G = 1.0
        self.mock_ics = np.random.rand(18)

    def test_calculate_system_energy(self):
        
        ke, pe, total_energy = calculate_system_energy(self.mock_result, self.mock_masses, self.mock_G)
        
        n_points = len(self.mock_result.t)
        
        self.assertIsInstance(ke, np.ndarray)
        self.assertEqual(ke.shape, (n_points,))
        
        self.assertIsInstance(pe, np.ndarray)
        self.assertEqual(pe.shape, (n_points,))
        
        self.assertIsInstance(total_energy, np.ndarray)
        self.assertEqual(total_energy.shape, (n_points,))

    def test_calculate_center_of_mass(self):
    
        com_pos, com_vel = calculate_center_of_mass(self.mock_result, self.mock_masses)
        
        n_points = len(self.mock_result.t)
        
        self.assertIsInstance(com_pos, np.ndarray)
        self.assertEqual(com_pos.shape, (3, n_points))
        
        self.assertIsInstance(com_vel, np.ndarray)
        self.assertEqual(com_vel.shape, (3, n_points))

    def test_perturb_initial_conditions(self):
        
        perturbed_ics = perturb_initial_conditions(self.mock_ics, magnitude=1e-5)
        
        self.assertIsInstance(perturbed_ics, np.ndarray)
        self.assertEqual(perturbed_ics.shape, self.mock_ics.shape)
        self.assertFalse(np.array_equal(self.mock_ics, perturbed_ics))
        difference = float(np.linalg.norm(perturbed_ics - self.mock_ics))
        self.assertAlmostEqual(difference, 1e-5, places=10)

if __name__ == '__main__':
    unittest.main()