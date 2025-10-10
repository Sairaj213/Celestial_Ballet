import streamlit as st
import numpy as np

def render_parameter_sliders(initial_state=None):

    st.sidebar.header("Body Properties")

    if initial_state is None:
        default_masses = [1.0, 1.0, 1.0]
        default_ics = np.array([
            0.97, -0.24, 0.0, 0.46, 0.43, 0.0,
           -0.97,  0.24, 0.0, 0.46, 0.43, 0.0,
            0.0,   0.0,  0.0,-0.93,-0.86, 0.0
        ])
    else:
        default_masses = initial_state['masses']
        default_ics = initial_state['initial_conditions']
        
    masses = []
    positions = []
    velocities = []

    for i in range(3):
        st.sidebar.subheader(f"Body {i+1}")
        cols = st.sidebar.columns(3)
        
        # Mass
        m = cols[0].number_input(f"Mass {i+1}", key=f"m{i}", value=default_masses[i], format="%.2f")
        masses.append(m)
        
        # Position Inputs
        px = cols[1].number_input(f"Pos X{i+1}", key=f"px{i}", value=default_ics[i*6 + 0], format="%.2f")
        py = cols[2].number_input(f"Pos Y{i+1}", key=f"py{i}", value=default_ics[i*6 + 1], format="%.2f")
        pz = cols[0].number_input(f"Pos Z{i+1}", key=f"pz{i}", value=default_ics[i*6 + 2], format="%.2f")
        positions.extend([px, py, pz])
        
        # Velocity Inputs
        vx = cols[1].number_input(f"Vel X{i+1}", key=f"vx{i}", value=default_ics[i*6 + 3], format="%.2f")
        vy = cols[2].number_input(f"Vel Y{i+1}", key=f"vy{i}", value=default_ics[i*6 + 4], format="%.2f")
        vz = cols[0].number_input(f"Vel Z{i+1}", key=f"vz{i}", value=default_ics[i*6 + 5], format="%.2f")
        velocities.extend([vx, vy, vz])

    initial_conditions_array = np.array([val for pair in zip(positions, velocities) for val in pair])

    final_ics = np.zeros(18)
    final_ics[0::6] = positions[0::3] 
    final_ics[1::6] = positions[1::3] 
    final_ics[2::6] = positions[2::3] 
    final_ics[3::6] = velocities[0::3] 
    final_ics[4::6] = velocities[1::3] 
    final_ics[5::6] = velocities[2::3] 


    return masses, final_ics
