import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import sympy as sp
from utils.latex_utils import format_equation_to_latex

def render_equations_viewer(equations_of_motion):

    st.header("Derived Equations of Motion (Newtonian)")
    st.write("The following equations govern the acceleration of each body.")
    
    body_labels = ["Body 1 (m₁)", "Body 2 (m₂)", "Body 3 (m₃)"]
    component_labels = ["ẍ", "ÿ", "z̈"] 
    
    for i in range(3):
        with st.expander(f"Equations for {body_labels[i]}", expanded=(i==0)):
            cols = st.columns(3)
            for j in range(3):
        
                eq = equations_of_motion[3 * i + j]
                label = f"{component_labels[j]}_{i+1}"
                latex_str = format_equation_to_latex(eq, label=label)
                cols[j].latex(latex_str)

