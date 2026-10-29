// ==============================================================================
// Program: vector_loop_demo.c
// Purpose: Demonstrating Compiler Vectorization (-O3 -mavx2 / -mavx512)
// ==============================================================================
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 2048000

void vector_accumulate(float* restrict a, float* restrict b, float* restrict c, int n) {
    for (int i = 0; i < n; ++i) {
        c[i] = a[i] * b[i] + 0.5f;
    }
}

int main() {
    float *a = (float*)aligned_alloc(64, SIZE * sizeof(float));
    float *b = (float*)aligned_alloc(64, SIZE * sizeof(float));
    float *c = (float*)aligned_alloc(64, SIZE * sizeof(float));

    for (int i = 0; i < SIZE; ++i) {
        a[i] = 1.5f;
        b[i] = 2.0f;
    }

    clock_t start = clock();
    vector_accumulate(a, b, c, SIZE);
    clock_t end = clock();

    double cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC * 1000.0;
    printf("Vector loop executed across %d elements in %.3f ms (c[0]=%.2f)\n", SIZE, cpu_time, c[0]);

    free(a);
    free(b);
    free(c);
    return 0;
}
