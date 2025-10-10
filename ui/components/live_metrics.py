import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import numpy as np
from utils.visualization_tools import calculate_system_energy
from utils.math_utils import calculate_closest_approach

def render_live_metrics(simulation_result, masses, G):

    if not simulation_result:
        st.info("Simulation has not run yet. Metrics will appear here.")
        return

    # --- Data Extraction ---
    time_index = -1 
    current_time = simulation_result.t[time_index]
    
    # Energy Calculation
    ke, pe, total_energy = calculate_system_energy(simulation_result, masses, G)
    initial_energy = total_energy[0]
    current_energy = total_energy[time_index]
    energy_delta_percent = ((current_energy - initial_energy) / initial_energy) * 100 if initial_energy != 0 else 0

    # --- NEW: Closest Approach Calculation ---
    closest_distance = calculate_closest_approach(simulation_result)

    # --- UI Rendering ---
    st.subheader("Live System Telemetry")
    cols = st.columns(3)

    cols[0].metric(
        label="Simulation Time (s)",
        value=f"{current_time:,.2f}"
    )
    
    cols[1].metric(
        label="Total System Energy (J)",
        value=f"{current_energy:,.3e}",
        delta=f"{energy_delta_percent:,.4f}% vs Initial",
        delta_color="normal"
    )

    # --- CORRECTED: Display the real value ---
    cols[2].metric(
        label="Closest Approach (m)",
        value=f"{closest_distance:,.3e}",
        help="Minimum distance between any two bodies during the entire simulation."
    )