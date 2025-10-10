import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import numpy as np
from utils.visualization_tools import plot_energy_conservation
from utils.math_utils import calculate_center_of_mass

def render_tab_analysis(simulation_result, masses, G):

    st.title("🧮 Analytical Insights")
    
    if simulation_result is None:
        st.info("Run a simulation to generate data for analysis.")
        return

    st.markdown("---")
    st.subheader("Energy Conservation Analysis")
    st.markdown("""
    In a closed gravitational system, the total energy (Kinetic + Potential) must be conserved. 
    A flat line for 'Total Energy' indicates a numerically stable and physically accurate simulation.
    """)
    energy_figure = plot_energy_conservation(simulation_result, masses, G)
    st.plotly_chart(energy_figure, use_container_width=True)

    st.markdown("---")
    st.subheader("Center of Mass (CoM) Stability")
    st.markdown("""
    With no external forces, the velocity of the system's center of mass should remain constant. 
    The plots below should show straight lines if the simulation is stable.
    """)
    com_pos, com_vel = calculate_center_of_mass(simulation_result, masses)
    com_df = pd.DataFrame({
        'Time': simulation_result.t,
        'CoM Velocity X': com_vel[0],
        'CoM Velocity Y': com_vel[1],
        'CoM Velocity Z': com_vel[2]
    })
    st.line_chart(com_df, x='Time', y=['CoM Velocity X', 'CoM Velocity Y', 'CoM Velocity Z'])
    
    st.markdown("---")
    st.subheader("Export Raw Data")
    st.markdown("Download the complete time-series data for the simulation as a CSV file.")
    
    column_names = []
    for i in range(3):
        for dim in ['x', 'y', 'z']:
            column_names.append(f'body{i+1}_pos_{dim}')
        for dim in ['x', 'y', 'z']:
            column_names.append(f'body{i+1}_vel_{dim}')

    export_df = pd.DataFrame(simulation_result.y.T, columns=column_names)
    export_df.insert(0, 'time', simulation_result.t)

    st.download_button(
        label="📥 Download as CSV",
        data=export_df.to_csv(index=False).encode('utf-8'),
        file_name='three_body_simulation_data.csv',
        mime='text/csv',
    )