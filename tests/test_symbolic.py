import unittest
import sympy as sp
from core.symbolic_setup import create_symbolic_system
from core.equations_builder import derive_equations_of_motion

class TestSymbolicModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.symbolic_system = create_symbolic_system()

    def test_create_symbolic_system_structure(self):

        self.assertIsInstance(self.symbolic_system, dict)
        self.assertIn('time', self.symbolic_system)
        self.assertIn('constants', self.symbolic_system)
        self.assertIn('states', self.symbolic_system)
        
        self.assertIsInstance(self.symbolic_system['time'], sp.Symbol)
        self.assertEqual(len(self.symbolic_system['constants']['masses']), 3)
        self.assertEqual(len(self.symbolic_system['states']['positions']), 9)
        self.assertEqual(len(self.symbolic_system['states']['velocities']), 9)
        self.assertEqual(len(self.symbolic_system['states']['accelerations']), 9)

    def test_derive_equations_of_motion(self):

        equations = derive_equations_of_motion(self.symbolic_system)
        self.assertEqual(len(equations), 9)
        for eq in equations:
            self.assertIsInstance(eq, sp.Eq)
        first_eq_str = str(equations[0])
        self.assertIn('G', first_eq_str)
        self.assertIn('m1', first_eq_str)
        self.assertIn('m2', first_eq_str)
        self.assertIn('m3', first_eq_str)
        self.assertIn('x1(t)', first_eq_str)
        self.assertIn('x2(t)', first_eq_str)
        self.assertIn('x3(t)', first_eq_str)

if __name__ == '__main__':
    unittest.main()