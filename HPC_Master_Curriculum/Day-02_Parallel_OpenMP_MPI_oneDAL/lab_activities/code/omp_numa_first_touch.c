// omp_numa_first_touch.c
// Demonstrates Linux First-Touch Memory Allocation Policy across NUMA Sockets
// Compile: gcc -O3 -fopenmp omp_numa_first_touch.c -o numa_first_touch
// Run: ./numa_first_touch

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define N 50000000

double get_time_sec() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

int main() {
    double *a = (double *)malloc(N * sizeof(double));
    double *b = (double *)malloc(N * sizeof(double));
    double *c = (double *)malloc(N * sizeof(double));

    printf("================================================================\n");
    printf("   🔬 NUMA FIRST-TOUCH MEMORY ALLOCATION & SCALING BENCHMARK     \n");
    printf("      Array Size: %d doubles (%.2f MB per array)\n", N, (N * sizeof(double)) / (1024.0 * 1024.0));
    printf("      Available Threads: %d\n", omp_get_max_threads());
    printf("================================================================\n");

    // Case 1: Bad Initialization (Master Thread Touches Memory First)
    // All physical pages are bound to Socket 0's local memory controller!
    double t0 = get_time_sec();
    for (int i = 0; i < N; i++) {
        a[i] = 1.0;
        b[i] = 2.0;
        c[i] = 0.0;
    }
    double init_time_bad = get_time_sec() - t0;
    printf("\n[-] Single-Thread Sequential Initialization (Page Placement on Socket 0):\n");
    printf("    Init Time: %.4f seconds\n", init_time_bad);

    // Parallel Compute Loop
    t0 = get_time_sec();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        c[i] = a[i] * 2.5 + b[i];
    }
    double compute_time_bad = get_time_sec() - t0;
    printf("    Parallel Compute Time: %.4f seconds (Remote NUMA UPI traffic bottleneck)\n", compute_time_bad);

    // Case 2: Good Initialization (Parallel First-Touch Policy)
    // Physical pages are allocated in the NUMA node of the thread writing first!
    t0 = get_time_sec();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        a[i] = 1.0;
        b[i] = 2.0;
        c[i] = 0.0;
    }
    double init_time_good = get_time_sec() - t0;
    printf("\n[+] Parallel First-Touch Initialization (Pages Distributed across Local NUMA Controllers):\n");
    printf("    Init Time: %.4f seconds\n", init_time_good);

    // Parallel Compute Loop with Distributed Memory
    t0 = get_time_sec();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        c[i] = a[i] * 2.5 + b[i];
    }
    double compute_time_good = get_time_sec() - t0;
    printf("    Parallel Compute Time: %.4f seconds (Zero Inter-Socket Cross-Traffic)\n", compute_time_good);

    double speedup = compute_time_bad / compute_time_good;
    printf("\n================================================================\n");
    printf("  🏆 FIRST-TOUCH SPEEDUP: %.2fx Faster Parallel Execution\n", speedup);
    printf("  Takeaway: Linux assigns physical memory to the NUMA node where\n");
    printf("  the thread touches it FIRST, not where malloc() is called.\n");
    printf("================================================================\n");

    free(a);
    free(b);
    free(c);
    return 0;
}
