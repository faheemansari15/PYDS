A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A.union(B))
print(B.union(A))

print(A & B)
print(A.intersection(B))
print(B.intersection(A))

print(A - B)
print(A.difference(B))
print(B - A)
print(B.difference(A)) 

print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A)) 