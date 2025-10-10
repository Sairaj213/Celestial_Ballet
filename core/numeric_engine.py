import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sympy as sp
import numpy as np
import os
import json
from scipy.integrate import solve_ivp
from core.system_converter import convert_to_first_order_system
from core.equations_builder import derive_equations_of_motion
from core.symbolic_setup import create_symbolic_system

def create_numeric_engine(first_order_system, symbolic_system):

    t = symbolic_system['time']
    G, masses = symbolic_system['constants']['G'], symbolic_system['constants']['masses']

    state_vector_q = first_order_system['state_vector']
    first_order_odes = first_order_system['first_order_odes']
    numeric_args = [t] + state_vector_q + [G] + masses
    raw_ode_function = sp.lambdify(
        numeric_args,
        first_order_odes,
        modules='numpy'
    )

    def engine_function(t, y, *params):

        function_inputs = [t] + list(y) + list(params)
        return raw_ode_function(*function_inputs)

    return engine_function

def load_state(filepath):

    with open(filepath, 'r') as f:
        state_data = json.load(f)

    masses = state_data['masses']
    initial_conditions = np.array(state_data['initial_conditions'])
    constants = state_data['constants']

    return masses, initial_conditions, constants


symbolic_system = create_symbolic_system()
equations_of_motion = derive_equations_of_motion(symbolic_system)
first_order_system = convert_to_first_order_system(equations_of_motion, symbolic_system)

numeric_engine = create_numeric_engine(first_order_system, symbolic_system)
print(f"Successfully created the numeric engine function: {type(numeric_engine)}")

G_val = 6.67430e-11
mass_vals = [1.989e30, 5.972e24, 7.347e22] 
constants = [G_val] + mass_vals

initial_state_vector = np.random.rand(18)
current_time = 0.0

try:
    derivatives = numeric_engine(current_time, initial_state_vector, *constants)
    print("\nEngine executed successfully.")
    print(f"Output is a NumPy array of shape: {derivatives.shape}")
    assert derivatives.shape == (18,)
except Exception as e:
    print(f"\nAn error occurred during engine execution: {e}")


def run_simulation(numeric_engine, initial_conditions, t_span, t_eval, constants):

    solution = solve_ivp(
        fun=numeric_engine,
        t_span=t_span,
        y0=initial_conditions,
        t_eval=t_eval,
        args=tuple(constants),
        dense_output=True, 
        method='RK45'    
    )
    return solution

