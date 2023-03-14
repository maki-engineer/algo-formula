N, V = map(int, input().split())
A    = list(map(int, input().split()))

for a in range(N - 1, -1, -1):
  if A[a] == V:
    print(a)
    break
else:
  print(-1)