# demo_tuples_and_sets.py
# Complete demonstration of ALL 12 Tuple methods/functions & ALL 15 Set methods

print("="*60)
print("     ALL 12 TUPLE METHODS & BUILT-IN FUNCTIONS            ")
print("="*60)

t = (10, 20, 30, 20, 40, 50)
print("Tuple:", t)
# 1. count, 2. index
print("1. count(20) :", t.count(20))
print("2. index(30) :", t.index(30))

# 3. len, 4. min, 5. max, 6. sum
print(f"3. len={len(t)}, 4. min={min(t)}, 5. max={max(t)}, 6. sum={sum(t)}")

# 7. sorted, 8. tuple conversion
print("7. sorted()  :", sorted(t))
print("8. tuple()   :", tuple([1, 2, 3]))

# 9. any, 10. all
print("9. any()     :", any((0, False, 5)))
print("10. all()    :", all((1, True, "hello")))

# 11. enumerate, 12. reversed
print("11. enumerate:", list(enumerate(t[:3])))
print("12. reversed :", list(reversed(t)))

print("\n" + "="*60)
print("     ALL 15 SET METHODS & SET ALGEBRA                     ")
print("="*60)

s = {1, 2, 3}
# 1. add, 2. update
s.add(4)
s.update([5, 6])
print("After add & update:", s)

# 3. remove, 4. discard, 5. pop, 6. clear, 7. copy
s.remove(4)
s.discard(99) # Won't raise error!
popped_elem = s.pop()
s_copy = s.copy()
print(f"Popped: {popped_elem} | Remaining: {s} | Copy: {s_copy}")

# Set Algebra with two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# 8. union, 9. intersection, 10. difference, 11. symmetric_difference
print("8. Union (A | B)               :", A | B)
print("9. Intersection (A & B)        :", A & B)
print("10. Difference (A - B)         :", A - B)
print("11. Symmetric Difference (A ^ B):", A ^ B)

# 12. issubset, 13. issuperset, 14. isdisjoint, 15. len
C = {1, 2}
print("12. C.issubset(A)  :", C.issubset(A))
print("13. A.issuperset(C):", A.issuperset(C))
print("14. A.isdisjoint(B):", A.isdisjoint(B))
print("15. len(A)         :", len(A))
