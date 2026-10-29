# ==============================================================================
# Program: mpi_ring_demo.py
# Purpose: Simulating MPI Ring Topology Message Passing
# ==============================================================================
import time

NUM_RANKS = 4

print("=" * 60)
print("      SIMULATED MPI DISTRIBUTED RING COMMUNICATION         ")
print("=" * 60)
print(f"[*] Initializing ring topology across {NUM_RANKS} distributed virtual ranks...")

token = 100
for step in range(NUM_RANKS):
    sender = step
    receiver = (step + 1) % NUM_RANKS
    print(f"  [Step {step + 1}] Rank {sender} --(Token {token})--> Passing to Rank {receiver}")
    token += 1
    time.sleep(0.05)

print("-" * 60)
print(f"[+] Ring cycle complete! Final token payload: {token}")
print("=" * 60)
