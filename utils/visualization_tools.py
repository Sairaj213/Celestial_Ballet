import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import plotly.graph_objects as go
import numpy as np

def calculate_system_energy(simulation_result, masses, G):

    states = simulation_result.y
    n_points = states.shape[1]
    
    ke = np.zeros(n_points)
    pe = np.zeros(n_points)
    
    m1, m2, m3 = masses
    mass_list = [m1, m2, m3]
    
    p1, p2, p3 = states[0:3, :], states[6:9, :], states[12:15, :]
    pos_list = [p1, p2, p3]

    v1, v2, v3 = states[3:6, :], states[9:12, :], states[15:18, :]
    vel_list = [v1, v2, v3]

    for i in range(3):
        v_squared = np.sum(vel_list[i]**2, axis=0)
        ke += 0.5 * mass_list[i] * v_squared
        
    r12 = np.linalg.norm(p1 - p2, axis=0)
    r13 = np.linalg.norm(p1 - p3, axis=0)
    r23 = np.linalg.norm(p2 - p3, axis=0)
    
    pe = -G * ((m1 * m2 / r12) + (m1 * m3 / r13) + (m2 * m3 / r23))
    
    total_energy = ke + pe
    
    return ke, pe, total_energy

def plot_energy_conservation(simulation_result, masses, G):
  
    t = simulation_result.t
    ke, pe, total_energy = calculate_system_energy(simulation_result, masses, G)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=ke, mode='lines', name='Kinetic Energy'))
    fig.add_trace(go.Scatter(x=t, y=pe, mode='lines', name='Potential Energy'))
    fig.add_trace(go.Scatter(x=t, y=total_energy, mode='lines', name='Total Energy', line=dict(width=4)))

    initial_energy = total_energy[0]
    final_energy = total_energy[-1]
    delta_percent = ((final_energy - initial_energy) / initial_energy) * 100 if initial_energy != 0 else 0

    fig.update_layout(
        title=f'Energy Conservation (Total Drift: {delta_percent:.4f}%)',
        xaxis_title='Time (s)',
        yaxis_title='Energy (Joules)',
        legend_title='Energy Type'
    )
    return fig

def plot_trajectory_3d(simulation_result, bodies_to_plot=[0, 1, 2], colors=None, trail_percentage=100):
    fig = go.Figure()
    if colors is None:
        colors = ['#636EFA', '#EF553B', '#00CC96']
    trajectory_data = simulation_result.y
    total_points = trajectory_data.shape[1]
    trail_points = int(total_points * (trail_percentage / 100))
    start_point = total_points - trail_points
    for i in bodies_to_plot:
        start_idx = i * 6
        x, y, z = (
            trajectory_data[start_idx, start_point:],
            trajectory_data[start_idx + 1, start_point:],
            trajectory_data[start_idx + 2, start_point:]
        )
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(width=4, color=colors[i % len(colors)]),
            name=f'Body {i+1}'
        ))
    fig.update_layout(
        title='Three-Body Problem Trajectories',
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z', aspectmode='data'),
        margin=dict(l=0, r=0, b=0, t=40),
        legend=dict(x=0.8, y=0.9)
    )
    return fig