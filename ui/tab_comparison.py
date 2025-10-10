import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import numpy as np
from core.chaos_tools import perturb_initial_conditions
from core.numeric_engine import run_simulation
from utils.visualization_tools import plot_trajectory_3d

def render_tab_comparison(numeric_engine, control_state):

    st.title("🦋 The Butterfly Effect")
    st.markdown("""
    Chaotic systems exhibit extreme sensitivity to initial conditions. Here, we run two
    simulations: the **Original** and a **Perturbed** version, where a tiny change
    has been made to the starting state. Observe how a nearly imperceptible difference
    can lead to wildly divergent outcomes over time.
    """)

    st.sidebar.markdown("---")
    st.sidebar.header("Chaos Lab Controls")
    perturbation_magnitude = st.sidebar.select_slider(
        "Perturbation Magnitude",
        options=[1e-12, 1e-10, 1e-8, 1e-6, 1e-4],
        value=1e-8,
        format_func=lambda x: f"{x:.0e}" 
    )
    
    run_comparison = st.sidebar.button("🔬 Run Chaos Experiment", use_container_width=True)
    st.sidebar.markdown("*(Uses parameters from 'Body Properties' above)*")


    if not run_comparison:
        st.info("Set parameters in the sidebar and click 'Run Chaos Experiment' to begin.")
        return

    with st.spinner("Running original and perturbed simulations..."):
    
        t_span = (0, control_state['duration'])
        t_eval = np.linspace(t_span[0], t_span[1], control_state['time_steps'])
        G_val = 1.0 
        engine_constants = [G_val] + control_state['masses']

        original_ics = control_state['initial_conditions']
        sim_original = run_simulation(numeric_engine, original_ics, t_span, t_eval, engine_constants)

        perturbed_ics = perturb_initial_conditions(original_ics, magnitude=perturbation_magnitude)
        sim_perturbed = run_simulation(numeric_engine, perturbed_ics, t_span, t_eval, engine_constants)

    st.success("Chaos experiment complete.")
    st.markdown("---")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Simulation")
        fig_original = plot_trajectory_3d(sim_original)
        st.plotly_chart(fig_original, use_container_width=True)

    with col2:
        st.subheader(f"Perturbed Simulation (Difference: {perturbation_magnitude:.0e})")
        fig_perturbed = plot_trajectory_3d(sim_perturbed)
        st.plotly_chart(fig_perturbed, use_container_width=True)