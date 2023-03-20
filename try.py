N, K = map(int, input().split())
A    = list(map(int, input().split()))

results = [(A[x], A[y]) for x in range(N) for y in range(x + 1, N) if A[x] + A[y] <= K]

print(len(results))