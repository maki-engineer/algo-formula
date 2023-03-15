N = int(input())
A = list(map(int, input().split()))

count = 0

for n in range(N):
  if n >= 1:
    if A[n] > A[n - 1]:
      count += 1

print(count)