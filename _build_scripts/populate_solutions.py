# populate_solutions.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    p = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote: {rel_path}")

# Day 2 Solution
write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/student_lab_practice/solutions_and_code/solution_mpi_ring.py", """
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

token = 100 if rank == 0 else None
if rank == 0:
    comm.send(token, dest=1, tag=0)
    token = comm.recv(source=size-1, tag=0)
    print(f"[Master Rank 0] Ring Token Finished with value: {token}")
else:
    token = comm.recv(source=rank-1, tag=0)
    token += 1
    next_dest = (rank + 1) % size
    comm.send(token, dest=next_dest, tag=0)
""")

# Day 3 Solution
write_f("Day-03_DeepLearning_TF_Slurm_Horovod/student_lab_practice/solutions_and_code/solution_slurm_job.slurm", """
#!/bin/bash
#SBATCH --job-name=test_cluster_job
#SBATCH --output=logs/job_%j.log
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:10:00

python3 -c "import os; print('Allocated Cores on Compute Node:', os.cpu_count())"
""")

# Day 4 Solution
write_f("Day-04_Distributed_Slurm_VTune_Profiling/student_lab_practice/solutions_and_code/solution_vtune_script.sh", """
#!/bin/bash
vtune -collect hotspots -result-dir ./my_report -- python3 -c "sum(range(50000000))"
vtune -report summary -result-dir ./my_report
""")

# Day 5 Solution
write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/student_lab_practice/solutions_and_code/solution_test_client.py", """
import requests

url = "http://localhost:8000/api/chat"
data = {"user_message": "Explain how Intel AMX accelerates matrix operations in 2 lines."}
resp = requests.post(url, json=data)
print("Response from Local OpenVINO Engine:")
print(resp.json()["reply"])
""")

print("All solution files written successfully.")
