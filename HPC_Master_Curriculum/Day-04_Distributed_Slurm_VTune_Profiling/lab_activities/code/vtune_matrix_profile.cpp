// vtune_matrix_profile.cpp
// Demonstrates Cache-Blocked vs Naive Matrix Multiplication for Intel VTune Top-Down TMAM Profiling
// Compile: icx -O3 -xHost -qopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile
//          or: g++ -O3 -fopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile

#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>
#include <omp.h>

constexpr int N = 1024;
constexpr int BLOCK_SIZE = 64; // Tuned for L1/L2 cache line (64 bytes)

void naive_gemm(const std::vector<float>& A, const std::vector<float>& B, std::vector<float>& C) {
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            float sum = 0.0f;
            for (int k = 0; k < N; ++k) {
                // Inefficient strided access on B: B[k * N + j] thrashes cache lines
                sum += A[i * N + k] * B[k * N + j];
            }
            C[i * N + j] = sum;
        }
    }
}

void cache_blocked_gemm(const std::vector<float>& A, const std::vector<float>& B, std::vector<float>& C) {
    #pragma omp parallel for collapse(2) schedule(static)
    for (int bi = 0; bi < N; bi += BLOCK_SIZE) {
        for (int bj = 0; bj < N; bj += BLOCK_SIZE) {
            for (int bk = 0; bk < N; bk += BLOCK_SIZE) {
                // Inner tiled loops fit comfortably inside L1/L2 cache
                for (int i = bi; i < std::min(bi + BLOCK_SIZE, N); ++i) {
                    for (int k = bk; k < std::min(bk + BLOCK_SIZE, N); ++k) {
                        float rA = A[i * N + k];
                        #pragma omp simd
                        for (int j = bj; j < std::min(bj + BLOCK_SIZE, N); ++j) {
                            C[i * N + j] += rA * B[k * N + j];
                        }
                    }
                }
            }
        }
    }
}

int main() {
    std::cout << "==========================================================" << std::endl;
    std::cout << "   INTEL VTUNE TMAM BENCHMARK: MATRIX MULTIPLICATION      " << std::endl;
    std::cout << "   Matrix Dimension: " << N << " x " << N << " (FP32)" << std::endl;
    std::cout << "   Threads: " << omp_get_max_threads() << std::endl;
    std::cout << "==========================================================" << std::endl;

    std::vector<float> A(N * N, 1.0f);
    std::vector<float> B(N * N, 2.0f);
    std::vector<float> C1(N * N, 0.0f);
    std::vector<float> C2(N * N, 0.0f);

    // 1. Naive GEMM (Memory Bound / L3 Cache Thrashing)
    std::cout << "[*] Profiling Naive GEMM (High Cache-Miss Rate)..." << std::endl;
    auto start = std::chrono::high_resolution_clock::now();
    naive_gemm(A, B, C1);
    auto end = std::chrono::high_resolution_clock::now();
    double time_naive = std::chrono::duration<double>(end - start).count();
    double gflops_naive = (2.0 * N * N * N) / (time_naive * 1e9);
    std::cout << "[-] Naive GEMM Time: " << time_naive << " s | Performance: " << gflops_naive << " GFLOP/s" << std::endl;

    // 2. Cache-Blocked GEMM (Compute Bound / High L1/L2 Residency)
    std::cout << "[*] Profiling Cache-Blocked Tiled GEMM (L1/L2 Optimized)..." << std::endl;
    start = std::chrono::high_resolution_clock::now();
    cache_blocked_gemm(A, B, C2);
    end = std::chrono::high_resolution_clock::now();
    double time_blocked = std::chrono::duration<double>(end - start).count();
    double gflops_blocked = (2.0 * N * N * N) / (time_blocked * 1e9);
    std::cout << "[+] Blocked GEMM Time: " << time_blocked << " s | Performance: " << gflops_blocked << " GFLOP/s" << std::endl;

    double speedup = time_naive / time_blocked;
    std::cout << "==========================================================" << std::endl;
    std::cout << "[✓] Cache Blocking Speedup: " << speedup << "x" << std::endl;
    std::cout << "==========================================================" << std::endl;

    return 0;
}
