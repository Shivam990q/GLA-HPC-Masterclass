# demo_basics_and_loops.py
# Run this live in class to demonstrate Conditionals, Loops, and Loop-Else

print("="*60)
print("     DEMO 1: CONDITIONALS & TERNARY EXPRESSIONS           ")
print("="*60)

marks = 85
# Clean Ternary Operator
grade = "Distinction" if marks >= 75 else "Pass"
print(f"Marks: {marks} -> Status: {grade}")

print("\n" + "="*60)
print("     DEMO 2: THE FOR-ELSE PRIME SEARCH ALGORITHM          ")
print("="*60)

num = 29
# Demonstrating loop-else: 'else' runs ONLY if no 'break' was hit
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f"{num} is composite (divisible by {i})")
        break
else:
    print(f"{num} is PRIME! (Loop finished without hitting break)")

print("\n" + "="*60)
print("     DEMO 3: NESTED LOOPS & PATTERN PRINTING              ")
print("="*60)
# Pyramid live demo
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
