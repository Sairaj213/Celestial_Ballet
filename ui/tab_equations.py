import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import sympy as sp
from ui.components.equations_viewer import render_equations_viewer

def render_tab_equations(symbolic_system, equations_of_motion):

    st.title("⚖️ The Symbolic Foundation")
    st.markdown("""
    This simulation is not built on hard-coded numbers. It begins with a pure,
    symbolic representation of Newtonian physics. Below are the foundational
    equations of motion derived in real-time by the SymPy engine.
    """)
    st.markdown("---")

    if equations_of_motion:
        render_equations_viewer(equations_of_motion)
    else:
        st.warning("Equations of motion have not been generated yet.")

    st.markdown("---")

    with st.expander("Show Symbolic Variables and Constants"):
        col1, col2 = st.columns(2)
        constants_latex = ", ".join([sp.latex(s) for s in symbolic_system['constants']['masses']])
        constants_latex += ", " + sp.latex(symbolic_system['constants']['G'])
        col1.subheader("Constants")
        col1.latex(constants_latex)

        positions_latex = ", ".join([sp.latex(s) for s in symbolic_system['states']['positions'][:3]])
        velocities_latex = ", ".join([sp.latex(s) for s in symbolic_system['states']['velocities'][:3]])
        col2.subheader("Dynamic Variables (for Body 1)")
        col2.latex(f"\\text{{Positions: }}{positions_latex}, ...")
        col2.latex(f"\\text{{Velocities: }}{velocities_latex}, ...")