#!/usr/bin/env bash
# ==============================================================================
# compile_and_run_all.sh
# GLA University — Day 2 Hands-On Automated Build and Execution Harness
# ==============================================================================

set -euo pipefail

echo "======================================================================"
echo "   ⚡ GLA UNIVERSITY: DAY 2 PARALLEL COMPUTING & oneDAL SUITE        "
echo "======================================================================"

# 1. Compile OpenMP Codes
echo -e "\n[*] [Step 1] Compiling OpenMP Multithreading Benchmarks..."
if command -v icpx &>/dev/null; then
    echo "    [+] Found Intel oneAPI DPC++/C++ Compiler (icpx)"
    icpx -qopenmp -O3 omp_multithreading.cpp -o omp_reduction
    icpx -qopenmp -O3 omp_false_sharing_benchmark.cpp -o omp_false_sharing
    icx -qopenmp -O3 omp_numa_first_touch.c -o numa_first_touch
elif command -v g++ &>/dev/null; then
    echo "    [!] icpx not found; falling back to GNU g++ / gcc"
    g++ -fopenmp -O3 omp_multithreading.cpp -o omp_reduction
    g++ -fopenmp -O3 omp_false_sharing_benchmark.cpp -o omp_false_sharing
    gcc -fopenmp -O3 omp_numa_first_touch.c -o numa_first_touch
else
    echo "    [X] No C++ compiler found!"
fi

# 2. Compile MPI Codes
echo -e "\n[*] [Step 2] Compiling MPI Distributed Codes..."
if command -v mpicxx &>/dev/null; then
    echo "    [+] Found MPI C++ Compiler (mpicxx)"
    mpicxx -O3 mpi_hello_cluster.cpp -o mpi_hello
else
    echo "    [!] mpicxx not found; install libopenmpi-dev or Intel MPI"
fi

# 3. Execute OpenMP Tests
if [ -f "./omp_reduction" ]; then
    echo -e "\n[*] [Step 3] Running OpenMP Vector Reduction..."
    ./omp_reduction
fi

if [ -f "./omp_false_sharing" ]; then
    echo -e "\n[*] [Step 4] Running OpenMP False Sharing Benchmark..."
    ./omp_false_sharing
fi

# 4. Execute Python Benchmarks
echo -e "\n[*] [Step 5] Running Intel NumPy & Pandas Benchmark..."
python3 intel_numpy_pandas_benchmark.py

echo -e "\n[*] [Step 6] Running 2D Domain Decomposition Simulation..."
python3 data_decomposition_grid.py

echo -e "\n[*] [Step 7] Running Intel Scikit-Learn (oneDAL) Benchmark..."
python3 intel_scikit_speedup.py

echo -e "\n======================================================================"
echo "  🏆 ALL DAY 2 BENCHMARKS COMPLETED SUCCESSFULLY!"
echo "======================================================================"
