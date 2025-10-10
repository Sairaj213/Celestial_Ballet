import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import plotly.graph_objects as go

from utils.visualization_tools import plot_trajectory_3d
from ui.components.live_metrics import render_live_metrics

def render_tab_simulation(simulation_result, masses, G):

    st.title("🌌 Live Simulation")
    
    plot_container = st.container()
    metrics_container = st.container()

    if simulation_result is None:
        plot_container.info("Click '▶️ Run Simulation' in the sidebar to begin.")
        fig = go.Figure()
        fig.update_layout(
            scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z', aspectmode='data'),
            title="Waiting for simulation data..."
        )
        plot_container.plotly_chart(fig, use_container_width=True)
        return

    with metrics_container:

        render_live_metrics(simulation_result, masses, G)

    with plot_container:
        st.subheader("Orbital Trajectories")
        
        max_time_index = len(simulation_result.t) - 1
        time_index = st.slider(
            "Time Scrubber", 
            min_value=0, 
            max_value=max_time_index, 
            value=max_time_index,
            help="Drag to view the state of the system at different times."
        )
        
        trajectory_figure = plot_trajectory_3d(simulation_result)
        
        colors = ['blue', 'red', 'green']
        for i in range(3):
            start_idx = i * 6
            trajectory_figure.add_trace(go.Scatter3d(
                x=[simulation_result.y[start_idx, time_index]],
                y=[simulation_result.y[start_idx + 1, time_index]],
                z=[simulation_result.y[start_idx + 2, time_index]],
                mode='markers',
                marker=dict(size=8, color=colors[i]),
                name=f'Body {i+1} (current)'
            ))
        
        st.plotly_chart(trajectory_figure, use_container_width=True)