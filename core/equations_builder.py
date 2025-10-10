import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sympy as sp
from sympy.physics.vector import ReferenceFrame

def derive_equations_of_motion(symbolic_system):

    G, (m1, m2, m3) = symbolic_system['constants']['G'], symbolic_system['constants']['masses']
    pos = symbolic_system['states']['positions']
    acc = symbolic_system['states']['accelerations']
    
    N = ReferenceFrame('N')
    p1 = pos[0]*N.x + pos[1]*N.y + pos[2]*N.z
    p2 = pos[3]*N.x + pos[4]*N.y + pos[5]*N.z
    p3 = pos[6]*N.x + pos[7]*N.y + pos[8]*N.z

    bodies = [
        {'mass': m1, 'pos': p1, 'acc': acc[0:3]},
        {'mass': m2, 'pos': p2, 'acc': acc[3:6]},
        {'mass': m3, 'pos': p3, 'acc': acc[6:9]}
    ]

    all_equations = []
    unit_vectors = [N.x, N.y, N.z]
    for i, body_i in enumerate(bodies):
        
        total_force = 0 * N.x
        for j, body_j in enumerate(bodies):
            if i == j:
                continue

            r_ij = body_j['pos'] - body_i['pos']
            distance = r_ij.magnitude()
 
            force_ij = (G * body_i['mass'] * body_j['mass'] / distance**3) * r_ij
            total_force += force_ij

        for component_index in range(3):
            mass_times_accel = body_i['mass'] * body_i['acc'][component_index]
            force_component = total_force.dot(unit_vectors[component_index])
            
            equation = sp.Eq(mass_times_accel, force_component)
            all_equations.append(equation)

    return all_equations

