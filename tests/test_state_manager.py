import unittest
import os
import json
import numpy as np
from core.state_manager import save_state, load_state

class TestStateManagerModule(unittest.TestCase):

    def setUp(self):

        self.test_dir = "tests/temp"
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_filepath = os.path.join(self.test_dir, "test_state.json")
        self.sample_constants = {'G': 1.0}
        self.sample_masses = [1.0, 2.0, 3.0]
        self.sample_ics = np.arange(18, dtype=float)

    def tearDown(self):
    
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)
        if os.path.exists(self.test_dir):
            if not os.listdir(self.test_dir):
                os.rmdir(self.test_dir)

    def test_save_state(self):
    
        save_state(self.test_filepath, self.sample_masses, self.sample_ics, self.sample_constants)
        self.assertTrue(os.path.exists(self.test_filepath))
    
        with open(self.test_filepath, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['constants'], self.sample_constants)
            self.assertEqual(data['masses'], self.sample_masses)
            self.assertEqual(data['initial_conditions'], self.sample_ics.tolist())

    def test_load_state_and_data_integrity(self):
        save_state(self.test_filepath, self.sample_masses, self.sample_ics, self.sample_constants)
        loaded_masses, loaded_ics, loaded_constants = load_state(self.test_filepath)
        self.assertEqual(loaded_constants, self.sample_constants)
        self.assertEqual(loaded_masses, self.sample_masses)
        self.assertIsInstance(loaded_ics, np.ndarray)
        np.testing.assert_array_equal(loaded_ics, self.sample_ics)

if __name__ == '__main__':
    unittest.main()