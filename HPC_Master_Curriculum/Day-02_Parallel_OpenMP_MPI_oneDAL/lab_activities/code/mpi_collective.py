# mpi_collective.py
# Run with: mpirun -n 4 python3 mpi_collective.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ARRAY_SIZE = 8

if rank == 0:
    data = np.arange(ARRAY_SIZE * size, dtype='i')
    print(f"[Master Node 0] Master Dataset: {data}")
else:
    data = None

# Scatter: Distribute chunks to every node
local_data = np.empty(ARRAY_SIZE, dtype='i')
comm.Scatter(data, local_data, root=0)

# Each node performs local computation
local_sum = np.sum(local_data)
print(f"[Node {rank}] Received chunk {local_data} | Local Sum = {local_sum}")

# Reduce: Sum all local sums into master rank
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"[Master Node 0] Final Global Reduced Sum: {global_sum}")
