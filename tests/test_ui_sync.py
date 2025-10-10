import unittest
from unittest.mock import MagicMock, patch
st_mock = MagicMock()

@patch('ui.sidebar_controls.st', st_mock)
@patch('ui.components.parameter_sliders.st', st_mock)
class TestUISyncModule(unittest.TestCase):

    def test_sidebar_controls_returns_correct_structure(self):
        
        from ui.sidebar_controls import render_sidebar
        control_state = render_sidebar()
        self.assertIsInstance(control_state, dict)
        expected_keys = [
            "selected_preset",
            "duration",
            "time_steps",
            "masses",
            "initial_conditions",
            "run_button_pressed",
            "stop_button_pressed",
        ]
        for key in expected_keys:
            self.assertIn(key, control_state, f"Key '{key}' is missing from the control state dictionary.")

    def test_parameter_sliders_returns_correct_structure(self):

        import numpy as np
        from ui.components.parameter_sliders import render_parameter_sliders
        st_mock.sidebar.columns.return_value = (MagicMock(), MagicMock(), MagicMock())
        masses, ics = render_parameter_sliders()
        self.assertIsInstance(masses, list)
        self.assertEqual(len(masses), 3)

        self.assertIsInstance(ics, np.ndarray)
        self.assertEqual(ics.shape, (18,))


if __name__ == '__main__':
    unittest.main()