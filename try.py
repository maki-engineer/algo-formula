N, M, K = map(int, input().split())
A    = list(map(int, input().split()))
B    = list(map(int, input().split()))

count = 0

for ai in range(N):
  for bi in range(M):
    if A[ai] + B[bi] == K: count += 1

print(count)