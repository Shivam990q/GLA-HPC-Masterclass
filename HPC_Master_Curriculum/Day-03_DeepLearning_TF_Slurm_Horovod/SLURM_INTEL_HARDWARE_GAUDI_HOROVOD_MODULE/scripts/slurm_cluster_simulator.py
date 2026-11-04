#!/usr/bin/env python3
"""
Slurm Cluster Workload Simulator
Simulates the exact behavior of slurmctld, slurmd, sbatch, squeue, and scancel
for classroom demonstrations and environments without active root daemon permissions.
"""
import time
import random
import sys

def main():
    print("==========================================================")
    print("       SLURM WORKLOAD MANAGER CLUSTER DEMO SIMULATOR      ")
    print("       GLA University Supercomputing Masterclass          ")
    print("==========================================================")
    
    job_id = random.randint(104500, 104999)
    print(f"\n[1] Submitting Batch Job: 'train_resnet_hpc.slurm'")
    print(f"[+] sbatch: Submitted batch job {job_id} to partition 'compute-ai'")
    
    print("\n[2] Inspecting Active Cluster Queue: 'squeue -u $USER'")
    print(f"{'JOBID':<8} {'PARTITION':<12} {'NAME':<16} {'USER':<10} {'ST':<4} {'TIME':<8} {'NODES':<6} {'NODELIST'}")
    print("-" * 80)
    print(f"{job_id:<8} {'compute-ai':<12} {'gla_dl_horovod':<16} {'shivam':<10} {'PD':<4} {'0:00':<8} {'2':<6} {'(Priority)'}")
    print("--> Explanation: Job state is 'PD' (PENDING) while slurmctld arbitrates node priority.")
    
    time.sleep(1.2)
    print(f"\n[3] Scheduler Dispatch: slurmd allocated compute nodes 'node[01-02]'")
    print(f"{'JOBID':<8} {'PARTITION':<12} {'NAME':<16} {'USER':<10} {'ST':<4} {'TIME':<8} {'NODES':<6} {'NODELIST'}")
    print("-" * 80)
    print(f"{job_id:<8} {'compute-ai':<12} {'gla_dl_horovod':<16} {'shivam':<10} {'R':<4} {'0:05':<8} {'2':<6} {'node[01-02]'}")
    print("--> Explanation: Job state is 'R' (RUNNING). slurmd spawned 8 MPI ranks with 8 CPUs/task.")
    
    time.sleep(1.0)
    print("\n[4] Querying Overall Cluster Health: 'sinfo'")
    print(f"{'PARTITION':<12} {'AVAIL':<8} {'TIMELIMIT':<12} {'NODES':<8} {'STATE':<10} {'NODELIST'}")
    print("-" * 80)
    print(f"{'compute-ai*':<12} {'up':<8} {'2:00:00':<12} {'2':<8} {'alloc':<10} {'node[01-02]'}")
    print(f"{'compute-ai*':<12} {'up':<8} {'2:00:00':<12} {'14':<8} {'idle':<10} {'node[03-16]'}")
    print(f"{'gaudi-cluster':<12} {'up':<8} {'8:00:00':<12} {'8':<8} {'idle':<10} {'gaudi[01-08]'}")
    
    print("\n[5] Job Execution Lifecycle Complete:")
    print(f"[+] Output captured to: /scratch/logs/gla_dl_horovod_{job_id}.out")
    print("==========================================================")

if __name__ == "__main__":
    main()

