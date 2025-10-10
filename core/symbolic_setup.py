import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sympy as sp
from sympy.physics.vector import dynamicsymbols

def create_symbolic_system():

    t = sp.Symbol('t')
    G = sp.Symbol('G')
    m1, m2, m3 = sp.symbols('m1 m2 m3')
    x1, y1, z1 = dynamicsymbols('x1 y1 z1')
    x2, y2, z2 = dynamicsymbols('x2 y2 z2')
    x3, y3, z3 = dynamicsymbols('x3 y3 z3')

    positions = [x1, y1, z1, x2, y2, z2, x3, y3, z3]

    velocities = [sp.diff(p, t) for p in positions]
    accelerations = [sp.diff(v, t) for v in velocities]
    system_manifest = {
        'time': t,
        'constants': {
            'G': G,
            'masses': [m1, m2, m3]
        },
        'states': {
            'positions': positions,
            'velocities': velocities,
            'accelerations': accelerations
        }
    }

    return system_manifest

symbolic_system = create_symbolic_system()
from pprint import pprint
pprint({k: type(v) for k, v in symbolic_system.items()})
print("\nSample Position Variable:", symbolic_system['states']['positions'][0])
print("Sample Velocity Variable:", symbolic_system['states']['velocities'][0])
print("Sample Acceleration Variable:", symbolic_system['states']['accelerations'][0])