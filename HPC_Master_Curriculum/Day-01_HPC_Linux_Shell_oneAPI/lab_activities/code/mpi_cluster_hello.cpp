// ==============================================================================
// Program: mpi_cluster_hello.cpp
// Purpose: Multi-node / Multi-process distributed communication demonstration
// ==============================================================================
#include <iostream>

#if __has_include(<mpi.h>)
#include <mpi.h>
#define HAS_MPI 1
#else
#define HAS_MPI 0
#endif

int main(int argc, char** argv) {
#if HAS_MPI
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    std::cout << "[MPI Rank " << rank << " of " << size << "] Hello from Cluster Host: " 
              << processor_name << std::endl;

    MPI_Finalize();
#else
    std::cout << "[Standalone Rank 0 of 1] MPI headers not found. Running single-node process simulation." << std::endl;
#endif
    return 0;
}
