N = int(input())
A = list(map(int, input().split()))

dp    = [0 for _ in range(N)]
dp[1] = A[1]

for i in range(2, N):
  dp[i] = min(A[i] + dp[i - 1], (2 * A[i]) + dp[i - 2])

print(dp[-1])