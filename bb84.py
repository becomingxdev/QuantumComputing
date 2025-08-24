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

    # --- Step 2: Alice encodes her bits into qubits ---
    all_qubits = []
    for i in range(KEY_LENGTH):
        # Create a new circuit for each qubit
        qc = QuantumCircuit(1, 1)


        # Get the specific bit and basis for this round (e.g., the 5th bit and 5th basis)
        current_bit = alice_bits[i]
        current_basis = alice_bases[i]

        # --- Z-basis logic (Basis is 0) ---
        # A qubit always starts as 0. If Alice's bit is 1, we need to flip it.
        if current_basis == 0 and current_bit == 1:
            qc.x(0) # Apply X-gate to flip 0 to 1

            # --- X-basis logic (Basis is 1) ---
            # To prepare in the X-basis, we always start with a Hadamard gate.
            # But if the bit is 1, we need to flip it first.
        elif current_basis == 1:
            if current_bit == 1:
                qc.x(0) # First, flip 0 to 1
            qc.h(0) # THEN, apply H-gate to put it in the X-basis
            
        all_qubits.append(qc)

        #Checking for error
        for k in all_qubits:
            if(k == -1):
                print("Error! restarting the process")
    print(f"\nAlice has prepared {len(all_qubits)} qubits to send to Bob.")


    # --- Step 3: Bob chooses his bases and measures the qubits ---
    # Bob generates his own random string of bases
    bob_bases = [random.randint(0, 1) for i in range(KEY_LENGTH)]
    print(f"Bob's chosen bases:   {bob_bases} (0=Z, 1=X)")

    bob_bits = []
    for i in range(KEY_LENGTH):
        # Get the specific circuit prepared by Alice
        qc = all_qubits[i]

        # If Bob's basis is X (1), he applies an H-gate BEFORE measuring
        if bob_bases[i] == 1:
            qc.h(0)
        
        # Bob always measures in the Z-basis
        qc.measure(0, 0)

        # Run the simulation for this single circuit
        simulator = Aer.get_backend('aer_simulator')
        result = simulator.run(qc, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        bob_bits.append(measured_bit)

    # ... (the code for Bob's measurement) ...
    print(f"Bob's measured bits:  {bob_bits}")


    # --- Step 4: Sifting Phase ---
    # Alice and Bob publicly compare their bases and keep only the bits where they match.
    
    sifted_key_alice = []
    sifted_key_bob = []
    
    for i in range(KEY_LENGTH):
        if alice_bases[i] == bob_bases[i]:
            sifted_key_alice.append(alice_bits[i])
            sifted_key_bob.append(bob_bits[i])

    print("\n--- Sifting Phase Complete ---")
    print(f"Alice's sifted key: {sifted_key_alice}")
    print(f"Bob's sifted key:   {sifted_key_bob}")


    # --- Step 5: Error Checking Phase ---
    # Alice and Bob compare a sample of their sifted keys to check for a spy.
    # In our simulation, we can just compare the whole key.
    
    errors = 0
    for i in range(len(sifted_key_alice)):
        if sifted_key_alice[i] != sifted_key_bob[i]:
            errors += 1
            
    qber = (errors / len(sifted_key_alice)) * 100 if sifted_key_alice else 0

    print("\n--- Final Results ---")
    if errors > 0:
        print(f"Errors found: {errors} ({qber:.2f}% QBER)")
        print("A spy may be present! Key is insecure. ABORT.")
        return None
    else:
        print("No errors found! The key is secure.")
        return sifted_key_alice


# This special if statement ensures the code only runs when you execute this file directly.
# It's a very important Python best practice!
if __name__ == "__main__":
    simulate_bb84()