import unittest
import numpy as np
from core.symbolic_setup import create_symbolic_system
from core.equations_builder import derive_equations_of_motion
from core.system_converter import convert_to_first_order_system
from core.numeric_engine import create_numeric_engine

class TestNumericModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    
        symbolic_system = create_symbolic_system()
        equations_of_motion = derive_equations_of_motion(symbolic_system)
        cls.first_order_system = convert_to_first_order_system(equations_of_motion, symbolic_system)
        cls.numeric_engine = create_numeric_engine(cls.first_order_system, symbolic_system)

    def test_convert_to_first_order_system(self):
        
        self.assertIsInstance(self.first_order_system, dict)
        self.assertIn('state_vector', self.first_order_system)
        self.assertIn('first_order_odes', self.first_order_system)
        self.assertEqual(len(self.first_order_system['state_vector']), 18)
        self.assertEqual(len(self.first_order_system['first_order_odes']), 18)

    def test_create_numeric_engine(self):
        
        self.assertTrue(callable(self.numeric_engine))
        t_val = 0.0
        y_vals = np.random.rand(18)
        param_vals = (1.0, 1.0, 1.0, 1.0) 
        
        try:
            derivatives = self.numeric_engine(t_val, y_vals, *param_vals)
            self.assertIsInstance(derivatives, np.ndarray)
            self.assertEqual(derivatives.shape, (18,))
            
        except Exception as e:
            self.fail(f"Numeric engine failed to execute: {e}")

if __name__ == '__main__':
    unittest.main()