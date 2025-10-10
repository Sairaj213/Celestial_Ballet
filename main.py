
import streamlit as st
import numpy as np
import time
import logging

# --- Core Logic Imports ---
from core.symbolic_setup import create_symbolic_system
from core.equations_builder import derive_equations_of_motion
from core.system_converter import convert_to_first_order_system
from core.numeric_engine import create_numeric_engine, run_simulation
from core.state_manager import load_state
from core.data_logger import setup_logger

# --- UI Imports ---
from ui.sidebar_controls import render_sidebar
from ui.dashboard import render_dashboard

# --- Utility Imports ---
from utils.performance_monitor import performance_timer

def main():
    """
    The main function that orchestrates the entire Streamlit application.
    """
    # === PHASE 1: SETUP & INITIALIZATION ===
    st.set_page_config(
        page_title="Three-Body Interactive Lab",
        page_icon="🪐",
        layout="wide"
    )

    # Initialize the application state once
    if 'app_state' not in st.session_state:
        # Set up the logger
        logger = setup_logger('ThreeBodySim')
        logger.info("--- New Session Initialized ---")

        # Perform the expensive, one-time symbolic computations
        with st.spinner("Initializing symbolic physics engine..."):
            symbolic_system = create_symbolic_system()
            equations_of_motion = derive_equations_of_motion(symbolic_system)
            first_order_system = convert_to_first_order_system(equations_of_motion, symbolic_system)
            numeric_engine = create_numeric_engine(first_order_system, symbolic_system)
        # Store all initialized components in a single state dictionary
        # Safely determine the log file path by checking for a FileHandler
        log_filepath = None
        for h in logger.handlers:
            if isinstance(h, logging.FileHandler):
                log_filepath = h.baseFilename
                break

        st.session_state.app_state = {
            "logger": logger,
            "symbolic_system": symbolic_system,
            "equations_of_motion": equations_of_motion,
            "numeric_engine": numeric_engine,
            "simulation_result": None,
            "log_filepath": log_filepath,
            "loaded_preset_data": None,
            "control_state": None,
            "performance_metrics": {},
        }
        logger.info("Symbolic engine initialized and cached.")
        logger.info("Symbolic engine initialized and cached.")

    # Retrieve the state for the current run
    app_state = st.session_state.app_state
    logger = app_state["logger"]

    # === PHASE 2: RENDER UI & CAPTURE USER INTENT ===
    control_state = render_sidebar()
    app_state['control_state'] = control_state # Store the latest controls

    # === PHASE 3: THE ACTION HANDLER ===
    # Check for a change in preset selection
    if control_state['selected_preset'] != st.session_state.get('last_selected_preset', ''):
        st.session_state.last_selected_preset = control_state['selected_preset']
        if control_state['selected_preset'] != "-- Manual Input --":
            try:
                filepath = f"data/presets/{control_state['selected_preset']}"
                masses, ics, consts = load_state(filepath)
                app_state['loaded_preset_data'] = {'masses': masses, 'initial_conditions': ics}
                logger.info(f"Loaded preset: {control_state['selected_preset']}")
                st.rerun() # Rerun to update the parameter sliders with preset data
            except FileNotFoundError:
                st.sidebar.error("Preset file not found.")
                app_state['loaded_preset_data'] = None

    # Handle the Stop/Reset button press
    if control_state['stop_button_pressed']:
        app_state['simulation_result'] = None
        logger.info("Simulation reset by user.")
        st.rerun()

    # Handle the Run Simulation button press
    if control_state['run_button_pressed']:
        with st.spinner("Calculating trajectories..."):
            logger.info("Simulation run triggered.")
            
            # Unpack simulation parameters from the control state
            masses = control_state['masses']
            initial_conditions = control_state['initial_conditions']
            duration = control_state['duration']
            time_steps = control_state['time_steps']

            # Assuming G is normalized for most presets unless specified
            G_val = 1.0 
            engine_constants = [G_val] + masses

            t_span = (0, duration)
            t_eval = np.linspace(t_span[0], t_span[1], time_steps)

            # --- Timed execution of the simulation ---
            start_time = time.perf_counter()
            result = run_simulation(
                app_state['numeric_engine'], initial_conditions, t_span, t_eval, engine_constants
            )
            end_time = time.perf_counter()
            run_time = end_time - start_time
            # --- Store results and metrics ---
            app_state['simulation_result'] = result
            app_state['performance_metrics']['perf_simulation_run'] = f"{run_time:.4f}"
            app_state['masses'] = masses
            app_state['constants'] = {'G': G_val}

            if result.success:
                logger.info(f"Simulation completed successfully in {run_time:.4f} seconds.")
            else:
                logger.error(f"Simulation failed: {result.message}")

    # === PHASE 4: RENDER THE MAIN DASHBOARD ===
    render_dashboard(app_state)


if __name__ == "__main__":
    main()