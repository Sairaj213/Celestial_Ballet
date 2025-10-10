import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import os
from ui.components.parameter_sliders import render_parameter_sliders

def render_sidebar():

    st.sidebar.title("🪐 Three-Body Lab")
    st.sidebar.markdown("---")
    st.sidebar.header("Load a Preset")
    preset_dir = "data/presets"
    try:
        preset_files = [f for f in os.listdir(preset_dir) if f.endswith('.json')]
        
        preset_options = ["-- Manual Input --"] + preset_files
        selected_preset = st.sidebar.selectbox("Choose a scenario", options=preset_options)
    except FileNotFoundError:
        st.sidebar.warning(f"Preset directory not found at '{preset_dir}'")
        selected_preset = "-- Manual Input --"
    
    st.sidebar.markdown("---")

    st.sidebar.header("Simulation Controls")
    duration = st.sidebar.slider("Duration (seconds)", min_value=1, max_value=500, value=20)
    time_steps = st.sidebar.slider("Time Steps", min_value=100, max_value=10000, value=2000)
    
    st.sidebar.markdown("---")
    loaded_state = st.session_state.get('loaded_preset_data', None)
    masses, initial_conditions = render_parameter_sliders(initial_state=loaded_state)

    st.sidebar.markdown("---")
    col1, col2 = st.sidebar.columns(2)
    run_button = col1.button("▶️ Run Simulation", use_container_width=True, type="primary")
    stop_button = col2.button("⏹️ Stop/Reset", use_container_width=True)

    control_state = {
        "selected_preset": selected_preset,
        "duration": duration,
        "time_steps": time_steps,
        "masses": masses,
        "initial_conditions": initial_conditions,
        "run_button_pressed": run_button,
        "stop_button_pressed": stop_button,
    }
    
    return control_state