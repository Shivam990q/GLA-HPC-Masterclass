# demo_recursion_visualizer.py
# Recursion call stack demonstration and memoization benchmark
import time
from functools import lru_cache

print("="*60)
print("     DEMO 1: VISUALIZING RECURSIVE CALL STACK             ")
print("="*60)

def visual_factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}-> factorial({n}) called (Stack Frame {depth})")
    if n <= 1:
        print(f"{indent}<- Base Case reached: returning 1")
        return 1
    result = n * visual_factorial(n - 1, depth + 1)
    print(f"{indent}<- Unwinding: returning {n} * fact({n-1}) = {result}")
    return result

visual_factorial(4)

print("\n" + "="*60)
print("     DEMO 2: TOWER OF HANOI (3 DISKS)                     ")
print("="*60)

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'Pole A', 'Pole C', 'Pole B')

print("\n" + "="*60)
print("     DEMO 3: MEMOIZATION WITH LRU_CACHE (FIBONACCI)       ")
print("="*60)

@lru_cache(maxsize=None)
def memo_fib(n):
    if n < 2:
        return n
    return memo_fib(n - 1) + memo_fib(n - 2)

t0 = time.perf_counter()
fib_val = memo_fib(100)
elapsed = time.perf_counter() - t0
print(f"Fibonacci(100) computed in {elapsed:.6f}s via @lru_cache:")
print(f"Result: {fib_val}")
