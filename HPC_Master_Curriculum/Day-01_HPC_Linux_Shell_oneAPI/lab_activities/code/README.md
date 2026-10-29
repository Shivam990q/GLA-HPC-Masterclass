# 💻 Day 1 Standalone Source Code Vault
## Executable C++, Python, and Shell Scripts for HPC Cluster Labs

This folder contains all standalone, runnable source code files for Day 1. Students can run them either inside Google Colab or directly in terminal sessions on Linux cluster nodes (`idc-vm`).

| Script / Program | Language | Execution Command | Description |
| :--- | :---: | :--- | :--- |
| `hpc_node_audit.sh` | Bash | `chmod +x hpc_node_audit.sh && ./hpc_node_audit.sh` | Probes CPU model, RAM, cache geometries, and kernel processes. |
| `orchestrator.sh` | Bash | `bash orchestrator.sh` | Runs end-to-end node audit and benchmark pipeline. |
| `compute_engine.py` | Python | `python3 compute_engine.py accelerated` | Compares single-thread Python loop vs vectorized NumPy math. |
| `sycl_device_query.cpp` | C++ | `g++ -std=c++20 sycl_device_query.cpp -o query && ./query` | Enumerate SYCL platforms, compute units, and max workgroup size. |
| `dpcpp_vector_add.cpp` | C++ / SYCL | `icpx -fsycl dpcpp_vector_add.cpp -o vec_add && ./vec_add` | 10M element vector addition benchmark using USM (`malloc_shared`). |
| `sycl_gemm.cpp` | C++ / OpenMP | `g++ -std=c++20 -O3 -fopenmp sycl_gemm.cpp -o gemm && ./gemm` | 512x512 2D Matrix multiplication ($O(N^3)$ computational benchmark). |
| `vector_loop_demo.c` | C | `gcc -O3 -mavx2 vector_loop_demo.c -o vec_loop && ./vec_loop` | Demonstrates compiler vectorization and SIMD loop auto-vectorization. |
| `mpi_cluster_hello.cpp`| C++ / MPI | `mpicxx mpi_cluster_hello.cpp -o mpi_hello && mpirun -n 4 ./mpi_hello` | Distributed 4-process MPI cluster communication demonstration. |
| `mpi_ring_demo.py` | Python | `python3 mpi_ring_demo.py` | Simulates MPI message token passing in a ring topology. |
| `setup_oneapi_env.sh` | Bash | `source setup_oneapi_env.sh` | Locates and sources Intel oneAPI environment variables. |
