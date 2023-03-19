X, Y, Z = map(int, input().split())
A    = list(map(int, input().split()))
B    = list(map(int, input().split()))
C    = list(map(int, input().split()))

count = 0

for ai in range(X):
  for bi in range(Y):
    for ci in range(Z):
      if A[ai] + B[bi] == C[ci]: count += 1

print(count)