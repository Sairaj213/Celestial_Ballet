import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import os
from core.numeric_engine import load_state

def perturb_initial_conditions(initial_conditions, magnitude=1e-9):

    perturbation = np.random.randn(*initial_conditions.shape)
    normalized_perturbation = perturbation / np.linalg.norm(perturbation)
    perturbed_ics = initial_conditions.copy() + normalized_perturbation * magnitude
    
    return perturbed_ics

