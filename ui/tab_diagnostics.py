import streamlit as st
import pandas as pd

def render_tab_diagnostics(simulation_result, log_filepath):

    st.title("⚙️ System Diagnostics")
    st.markdown("A look into the computational engine room.")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("ODE Solver Report")
        if simulation_result:
            solver_status = "Success" if simulation_result.success else "Failed"
            st.metric(label="Solver Status", value=solver_status)
            
            st.metric(label="Number of Function Evaluations", value=simulation_result.nfev)
            
            st.metric(label="Reason for Termination", value=simulation_result.message)
        else:
            st.info("Run a simulation to see the solver report.")

    with col2:
        st.subheader("Performance Metrics")
        sym_time = st.session_state.app_state['performance_metrics'].get('perf_symbolic_derivation', 'N/A')
        num_time = st.session_state.app_state['performance_metrics'].get('perf_numeric_engine_creation', 'N/A')
        sim_time = st.session_state.app_state['performance_metrics'].get('perf_simulation_run', 'N/A')

        st.text(f"Symbolic Derivation: {sym_time} s")
        st.text(f"Numeric Engine Creation: {num_time} s")
        st.text(f"Simulation Run: {sim_time} s")

    st.markdown("---")

    st.subheader("Simulation Event Log")
    try:
        with open(log_filepath, 'r') as f:
            log_content = f.read()
            st.code(log_content, language='log')
    except (FileNotFoundError, TypeError):
        st.warning("No log file found. Run a simulation to generate logs.")