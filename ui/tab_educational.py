import streamlit as st

def render_tab_educational():

    st.title("💡 Educational Guide")
    st.markdown("Understanding the Three-Body Problem and this simulator.")
    st.markdown("---")

    with st.expander("What is the Three-Body Problem?", expanded=True):
        st.markdown("""
        The **Three-Body Problem** is a classic challenge in physics and celestial mechanics. 
        The goal is to determine the individual motions of three point masses, bearing in mind 
        only their mutual gravitational attractions.

        - **Why is it famous?** Unlike the two-body problem (e.g., a single planet around a sun), 
          there is no general closed-form solution. The system is inherently **chaotic**, 
          meaning its long-term behavior is practically impossible to predict with perfect accuracy.

        - **What does chaotic mean?** It means the system exhibits extreme sensitivity to its 
          **initial conditions**. A minuscule change in the starting position or velocity of one 
          body can lead to completely different trajectories over time. This is often called the 
          **Butterfly Effect**.
        """)

    with st.expander("How to Use This Simulator"):
        st.markdown("""
        1.  **Sidebar Controls**: Use the sliders and buttons on the left to set up your universe.
            - You can manually input masses, positions, and velocities.
            - Alternatively, select a **Preset** for a well-known scenario, like the stable 'Figure-Eight' orbit.
        
        2.  **Run Simulation**: Click the 'Run Simulation' button. The engine will:
            - Symbolically derive the equations of motion using **SymPy**.
            - Convert them into a fast numerical function.
            - Solve the system over time using a numerical integrator from **SciPy**.

        3.  **Analyze the Results**: Explore the different tabs to understand the outcome.
            - **Live Simulation**: Watch the beautiful and complex dance of the bodies.
            - **Analytical Insights**: Check the graphs to verify the physics. Is energy conserved?
            - **Chaos Comparison Lab**: See the Butterfly Effect in action by comparing two almost identical simulations.
        """)

    with st.expander("Interpreting the Analysis Tab"):
        st.markdown("""
        - **Energy Conservation Plot**: This is your most important diagnostic tool. For a simulation to be
          physically valid, the **Total Energy** (black line) must remain nearly constant. If it drifts up or down,
          it indicates that numerical errors are accumulating in the solver, and the results may not be reliable.

        - **Center of Mass Velocity**: In the absence of external forces, the overall center of mass of the
          system should move in a straight line at a constant speed. This plot should therefore show flat lines.
          It's another key check on the simulation's physical accuracy.
        """)