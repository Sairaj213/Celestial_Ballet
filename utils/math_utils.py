import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from core.numeric_engine import run_simulation
from core.numeric_engine import load_state
from core.symbolic_setup import create_symbolic_system
from core.equations_builder import derive_equations_of_motion
from core.system_converter import convert_to_first_order_system
from core.numeric_engine import create_numeric_engine

def calculate_closest_approach(simulation_result):

    states = simulation_result.y
    p1, p2, p3 = states[0:3, :], states[6:9, :], states[12:15, :]

    r12 = np.linalg.norm(p1 - p2, axis=0)
    r13 = np.linalg.norm(p1 - p3, axis=0)
    r23 = np.linalg.norm(p2 - p3, axis=0)
    min_r12 = np.min(r12)
    min_r13 = np.min(r13)
    min_r23 = np.min(r23)

    return min(min_r12, min_r13, min_r23)


def calculate_center_of_mass(simulation_result, masses):

    states = simulation_result.y
    total_mass = sum(masses)
    
    p1, p2, p3 = states[0:3, :], states[6:9, :], states[12:15, :]
    v1, v2, v3 = states[3:6, :], states[9:12, :], states[15:18, :]
    
    m1, m2, m3 = masses
    
    com_position = (m1 * p1 + m2 * p2 + m3 * p3) / total_mass
    com_velocity = (m1 * v1 + m2 * v2 + m3 * v3) / total_mass
    
    return com_position, com_velocity