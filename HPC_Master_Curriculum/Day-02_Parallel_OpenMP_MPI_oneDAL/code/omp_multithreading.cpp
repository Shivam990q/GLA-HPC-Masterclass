#include <iostream>
#include <omp.h>
#include <vector>
#include <chrono>

int main() {
    const int SIZE = 100000000;
    std::vector<double> a(SIZE, 1.0);
    double sum = 0.0;

    std::cout << "[*] Starting OpenMP Parallel Reduction on " << omp_get_max_threads() << " threads..." << std::endl;
    auto t0 = std::chrono::high_resolution_clock::now();

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < SIZE; i++) {
        sum += a[i] * 0.5;
    }

    auto t1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = t1 - t0;

    std::cout << "[+] OpenMP Sum Result: " << sum << std::endl;
    std::cout << "[+] Computation Time : " << elapsed.count() << " seconds" << std::endl;
    return 0;
}
