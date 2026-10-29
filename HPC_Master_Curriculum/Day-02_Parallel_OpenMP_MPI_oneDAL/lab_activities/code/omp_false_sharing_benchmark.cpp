// omp_false_sharing_benchmark.cpp
// Demonstrates L1 Data Cache Line Bouncing (False Sharing) vs 64-byte Cache-Aligned Padding
// Compile: g++ -O3 -fopenmp omp_false_sharing_benchmark.cpp -o false_sharing_bench
// Run: ./false_sharing_bench

#include <iostream>
#include <vector>
#include <chrono>
#include <omp.h>

const int ITERATIONS = 100000000;
const int MAX_THREADS = 8;

// Struct WITHOUT padding: All elements sit on the same 64-byte cache line
struct UnpaddedData {
    int count;
};

// Struct WITH padding: Explicitly aligned to 64 bytes (L1 cache line size)
struct alignas(64) PaddedData {
    int count;
    char pad[60]; // Pad remaining bytes to guarantee isolation
};

int main() {
    int num_threads = omp_get_max_threads();
    std::cout << "================================================================" << std::endl;
    std::cout << "   ⚡ OPENMP FALSE SHARING BENCHMARK (MESI PROTOCOL PHYSICS)     " << std::endl;
    std::cout << "      Active Threads: " << num_threads << std::endl;
    std::cout << "      Iterations per Thread: " << ITERATIONS << std::endl;
    std::cout << "================================================================" << std::endl;

    // Test 1: False Sharing (All threads write to adjacent array elements)
    UnpaddedData bad_array[MAX_THREADS];
    for (int i = 0; i < MAX_THREADS; i++) bad_array[i].count = 0;

    auto t0 = std::chrono::high_resolution_clock::now();
    #pragma omp parallel num_threads(num_threads)
    {
        int tid = omp_get_thread_num();
        for (int i = 0; i < ITERATIONS; i++) {
            bad_array[tid].count++;
        }
    }
    auto t1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> bad_time = t1 - t0;
    std::cout << "\n[-] [CASE 1: FALSE SHARING ACTIVE] (Unpadded 64-byte Contention):" << std::endl;
    std::cout << "    Execution Time: " << bad_time.count() << " seconds" << std::endl;

    // Test 2: Cache-Aligned / Padded (Zero False Sharing)
    PaddedData good_array[MAX_THREADS];
    for (int i = 0; i < MAX_THREADS; i++) good_array[i].count = 0;

    auto t2 = std::chrono::high_resolution_clock::now();
    #pragma omp parallel num_threads(num_threads)
    {
        int tid = omp_get_thread_num();
        for (int i = 0; i < ITERATIONS; i++) {
            good_array[tid].count++;
        }
    }
    auto t3 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> good_time = t3 - t2;
    std::cout << "\n[+] [CASE 2: CACHE-ALIGNED PADDING] (Zero Invalidation Traffic):" << std::endl;
    std::cout << "    Execution Time: " << good_time.count() << " seconds" << std::endl;

    double speedup = bad_time.count() / good_time.count();
    std::cout << "\n================================================================" << std::endl;
    std::cout << "  🏆 RESULT: Cache-Aligned Architecture is " << speedup << "x FASTER!" << std::endl;
    std::cout << "  Architectural Insight: Eliminating MESI cache line bouncing" << std::endl;
    std::cout << "  prevents cross-core bus invalidation storms." << std::endl;
    std::cout << "================================================================" << std::endl;

    return 0;
}
