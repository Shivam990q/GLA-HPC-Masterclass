#!/usr/bin/env python3
"""
mpi_point_to_point.py
Demonstrates Point-to-Point Communication: Non-Blocking vs Blocking Token Ring
Run with: mpirun -n 4 python3 mpi_point_to_point.py
"""

from mpi4py import MPI
import time
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

next_rank = (rank + 1) % size
prev_rank = (rank - 1 + size) % size

print(f"[*] [Rank {rank}/{size}] Initialized. Neighbor topology: Prev={prev_rank} -> Next={next_rank}")
comm.Barrier()

# --- Part 1: Blocking Token Ring ---
token = 42 if rank == 0 else -1

t0 = time.time()
if rank == 0:
    print("\n--- Starting Blocking Token Ring ---")
    comm.send(token, dest=next_rank, tag=101)
    received_token = comm.recv(source=prev_rank, tag=101)
    print(f"[Rank 0] Successfully received back token: {received_token} in {time.time()-t0:.6f}s")
else:
    received_token = comm.recv(source=prev_rank, tag=101)
    print(f"[Rank {rank}] Received token {received_token}, forwarding to Rank {next_rank}")
    comm.send(received_token + 1, dest=next_rank, tag=101)

comm.Barrier()

# --- Part 2: Non-Blocking (Isend / Irecv) Overlapping Computation ---
if rank == 0:
    print("\n--- Starting Non-Blocking Token Ring (Computation/Communication Overlap) ---")

send_buf = np.array([rank * 100], dtype='i')
recv_buf = np.empty(1, dtype='i')

# Post non-blocking receive first to prevent buffer starvation
req_recv = comm.Irecv(recv_buf, source=prev_rank, tag=202)
# Post non-blocking send
req_send = comm.Isend(send_buf, dest=next_rank, tag=202)

# Simulate intensive local compute while data is in-flight across the cluster
local_math_work = 0
for i in range(100_000):
    local_math_work += (i * rank) % 17

# Wait for communication to finalize
req_send.Wait()
req_recv.Wait()

print(f"[Rank {rank}] Non-blocking transfer complete! Received value: {recv_buf[0]} from Rank {prev_rank} (Local Compute Checksum: {local_math_work})")

comm.Barrier()
if rank == 0:
    print("\n[+] Point-to-Point non-blocking cluster pipeline finished successfully with 0 deadlocks!")
