"""
This is the code for BB84 Qunatum protocol to generate a sifted key. And establish a secure connection between two people.
Coded by: Dev Hitesh Desai
Github Profile: becomingxdev
"""

#Import section
import random
from qiskit import QuantumCircuit
from qiskit_aer import Aer

def simulate_bb84():
    print("--- Starting BB84 Protocol Simulation ---")
    # Let's define the length of our key
    KEY_LENGTH = 16

    # --- Step 1: Alice prepares her bits and bases ---
    
    # Alice generates a random string of bits
    alice_bits = [random.randint(0, 1) for i in range(KEY_LENGTH)]

    # Alice generates a random string of bases
    # We'll use 0 for the Z-basis ('rectilinear') and 1 for the X-basis ('diagonal')
    alice_bases = [random.randint(0, 1) for i in range(KEY_LENGTH)]

    print(f"Alice's secret bits:  {alice_bits}")
    print(f"Alice's chosen bases: {alice_bases} (0=Z, 1=X)")

    # The rest of our code will go here...

# This line runs the function when you execute the script
simulate_bb84()