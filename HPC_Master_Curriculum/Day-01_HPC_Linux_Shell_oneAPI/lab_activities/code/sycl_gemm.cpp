// ==============================================================================
// Program: sycl_gemm.cpp
// Purpose: Parallel Matrix Multiplication (GEMM: C = A x B)
// ==============================================================================
#include <iostream>
#include <vector>
#include <chrono>

constexpr int N = 512; // 512x512 matrix

int main() {
    std::cout << "==========================================================" << std::endl;
    std::cout << "      PARALLEL MATRIX MULTIPLICATION (GEMM) BENCHMARK      " << std::endl;
    std::cout << "==========================================================" << std::endl;
    std::cout << "[*] Matrix Dimensions: " << N << " x " << N << " floats" << std::endl;

    std::vector<float> a(N * N, 1.0f);
    std::vector<float> b(N * N, 2.0f);
    std::vector<float> c(N * N, 0.0f);

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel for collapse(2)
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            float sum = 0.0f;
            for (int k = 0; k < N; ++k) {
                sum += a[i * N + k] * b[k * N + j];
            }
            c[i * N + j] = sum;
        }
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duration = end - start;

    double gflops = (2.0 * N * N * N * 1e-9) / (duration.count() * 1e-3);
    std::cout << "[+] GEMM Computation Time : " << duration.count() << " ms" << std::endl;
    std::cout << "[+] Floating-Point Perf   : " << gflops << " GFLOPs" << std::endl;
    std::cout << "[+] Result Verification   : C[0,0] = " << c[0] 
              << (c[0] == N * 2.0f ? " (✅ CORRECT)" : " (❌ MISMATCH)") << std::endl;
    std::cout << "==========================================================" << std::endl;
    return 0;
}
