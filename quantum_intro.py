# Import the tools we need from Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
# --- Step 1: Build the Circuit ---

# Create a circuit with 1 quantum bit and 1 classical bit to store the result
qc = QuantumCircuit(1, 1)

# Apply the Hadamard gate (H-gate) to our qubit. This puts it in superposition.
qc.h(0)

# Measure the qubit. This collapses the superposition into a 0 or 1.
qc.measure(0, 0)

# Let's see the circuit we built!
print("Our quantum circuit:")
print(qc)


# --- Step 2: Run the Circuit ---

# Get the ideal quantum simulator
simulator = Aer.get_backend('aer_simulator')

# Prepare the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Run the circuit on the simulator 1000 times
job = simulator.run(compiled_circuit, shots=1000)

# Grab the results
results = job.result()
counts = results.get_counts(compiled_circuit)

print("\nResults of 1000 measurements:")
print(counts)