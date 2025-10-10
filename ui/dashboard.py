import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from ui.tab_simulation import render_tab_simulation
from ui.tab_equations import render_tab_equations
from ui.tab_analysis import render_tab_analysis
from ui.tab_diagnostics import render_tab_diagnostics
from ui.tab_comparison import render_tab_comparison
from ui.tab_aesthetic import render_tab_aesthetic
from ui.tab_educational import render_tab_educational

def render_dashboard(app_state):

    st.title("Three-Body Problem Interactive Lab")

    (
        tab1, tab2, tab3, tab4, tab5, tab6, tab7
    ) = st.tabs([
        "🌌 Live Simulation",
        "⚖️ Mathematical Derivation",
        "🧮 Analytical Insights",
        "⚙️ System Diagnostics",
        "🦋 Chaos Comparison Lab",
        "🎨 Aesthetic Controls",
        "💡 Educational Guide",
    ])

    with tab1:
        render_tab_simulation(
            simulation_result=app_state.get('simulation_result'),
            masses=app_state.get('masses'),
            G=app_state.get('constants', {}).get('G')
        )

    with tab2:
        render_tab_equations(
            symbolic_system=app_state.get('symbolic_system'),
            equations_of_motion=app_state.get('equations_of_motion')
        )

    with tab3:
        render_tab_analysis(
            simulation_result=app_state.get('simulation_result'),
            masses=app_state.get('masses'),
            G=app_state.get('constants', {}).get('G')
        )

    with tab4:
        render_tab_diagnostics(
            simulation_result=app_state.get('simulation_result'),
            log_filepath=app_state.get('log_filepath')
        )

    with tab5:
        render_tab_comparison(
            numeric_engine=app_state.get('numeric_engine'),
            control_state=app_state.get('control_state')
        )

    with tab6:
        render_tab_aesthetic()

    with tab7:
        render_tab_educational()