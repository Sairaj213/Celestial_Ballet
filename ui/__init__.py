import os
import sys

# Ensure project root is in sys.path
root = os.path.abspath(os.path.dirname(__file__))
if root not in sys.path:
    sys.path.append(root)
