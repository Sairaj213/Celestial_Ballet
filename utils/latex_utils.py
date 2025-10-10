
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sympy as sp
from core.equations_builder import derive_equations_of_motion
from core.symbolic_setup import create_symbolic_system

def format_equation_to_latex(equation, label=""):

    latex_str = sp.latex(equation)
    if label:
        return f"{label}: \\quad {latex_str}"
    return latex_str

try:
    
    
    symbolic_system = create_symbolic_system()
    equations_of_motion = derive_equations_of_motion(symbolic_system)

    eq_to_format = equations_of_motion[0]
    latex_output = format_equation_to_latex(eq_to_format, label="\\ddot{x}_1")

    print("Generated LaTeX String:")
    print(latex_output)

    from IPython.display import display, Math
    print("\nRendered LaTeX in Jupyter:")
    display(Math(latex_output))
    
except NameError:
    print("Please ensure the 'equations_of_motion' variable is available from a previous step.")
except Exception as e:
    print(f"An error occurred during verification: {e}")