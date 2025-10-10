import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import numpy as np
import os

def save_state(filepath, masses, initial_conditions, constants):

    state_data = {
        'constants': constants,
        'masses': masses,
        'initial_conditions': initial_conditions.tolist() 
    }
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w') as f:
        json.dump(state_data, f, indent=4)

def load_state(filepath):

    with open(filepath, 'r') as f:
        state_data = json.load(f)
        
    masses = state_data['masses']
    initial_conditions = np.array(state_data['initial_conditions'])
    constants = state_data['constants']
    
    return masses, initial_conditions, constants


preset_name = "chaotic_start.json"

save_path = os.path.join("data", "presets", preset_name)

sim_constants = {'G': 6.67430e-11}
sim_masses = [1.0e26, 1.0e26, 1.0e26]
sim_initial_conditions = np.array([
    # Body 1: Pos(x,y,z), Vel(x,y,z)
    0, 0, 0,      0, 500, 0,
    # Body 2
    4.0e8, 0, 0,  0, 0, 1000,
    # Body 3
    -4.0e8, 0, 0, 0, 0, -1000
])

try:
    save_state(save_path, sim_masses, sim_initial_conditions, sim_constants)
    print(f"Successfully saved state to: {save_path}")
    assert os.path.exists(save_path)
except Exception as e:
    print(f"An error occurred during save: {e}")

try:
    loaded_masses, loaded_ics, loaded_constants = load_state(save_path)
    print(f"\nSuccessfully loaded state from: {save_path}")
    
    assert sim_constants == loaded_constants
    assert sim_masses == loaded_masses
    assert np.array_equal(sim_initial_conditions, loaded_ics)
    print("\nData integrity verified: Loaded data matches original data.")
    print(f"Loaded {len(loaded_masses)} masses and an initial condition vector of shape {loaded_ics.shape}.")
except Exception as e:
    print(f"\nAn error occurred during load: {e}")