N, M = map(int, input().split())
A    = list(map(int, input().split()))
B    = list(map(int, input().split()))

count = 0

for ai in range(N):
  for bi in range(M):
    if A[ai] > B[bi]: count += 1

print(count)