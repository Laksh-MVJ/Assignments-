
first_8 = digits[:8]
A = set()
B = set()
for x in first_8:
    A.add(x * 7)
    B.add(x * 9)
print("A =", A)
print("B =", B)

print("vi. Union:", A.union(B))
print("vii. Intersection:", A.intersection(B))

print("viii. A - B:", A.difference(B))
print("B - A:", B.difference(A))

print("ix. Symmetric difference:", A.symmetric_difference(B))

print("x. Is A subset of B?", A.issubset(B))
print("Is B superset of A?", B.issuperset(A))
X = int(input("xi. Enter a value to remove from A: "))
A.discard(X)
print("A after discard:", A)