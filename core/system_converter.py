import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sympy as sp

def convert_to_first_order_system(equations_of_motion, symbolic_system):

    positions = symbolic_system['states']['positions']
    velocities = symbolic_system['states']['velocities']

    accelerations = symbolic_system['states']['accelerations']
    accel_solutions = sp.solve(equations_of_motion, accelerations)

    state_vector_q = positions + velocities
    first_order_defs = velocities

    first_order_accels = [accel_solutions[accel] for accel in accelerations]
    first_order_odes = first_order_defs + first_order_accels
    
    return {
        'state_vector': state_vector_q,
        'first_order_odes': first_order_odes
    }

