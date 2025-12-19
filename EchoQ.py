from braket.circuits import Circuit
from braket.aws import AwsDevice
import matplotlib.pyplot as plt
import csv

# 1. Use the IonQ device that's ONLINE for you
device = AwsDevice("arn:aws:braket:eu-north-1::device/qpu/iqm/Emerald")

# 2. Build 2-qubit EchoQ circuit (q0, q1)
circuit = Circuit()

# Put q0 into superposition
circuit.h(0)

# Entangle q1 with q0
circuit.cnot(0, 1)

# IonQ requires all used qubits to be measured -> measure q0 and q1
circuit.measure(0)
circuit.measure(1)

print("EchoQ 2-qubit circuit:")
print(circuit)

# 3. Run 
shots = 100 
print(f"Running with {shots} shots...")

task = device.run(circuit, shots=shots)
result = task.result()

counts = result.measurement_counts  # e.g. {'00': n, '11': n, '01': n, '10': n}
print("Real hardware counts (q0q1):")
print(counts)

# 4. Save results to CSV
csv_file = "echoq_2qubit_q0q1_results.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Outcome (q0q1)", "Count"])
    for outcome, count in counts.items():
        writer.writerow([outcome, count])

print(f"Saved CSV: {csv_file}")

# 5. Plot histogram
plt.bar(counts.keys(), counts.values())
plt.title("EchoQ 2-qubit (q0,q1) on IonQ Aria-1")
plt.xlabel("Outcome (q0q1)")
plt.ylabel("Counts")
plt.show()
