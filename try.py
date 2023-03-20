N = int(input())
A = list(map(int, input().split()))

count = 0

for a in range(N):
  for b in range(a + 1, N):
    for c in range(b + 1, N):
      if max(A[a], A[b], A[c]) == A[b]: count += 1

print(count)