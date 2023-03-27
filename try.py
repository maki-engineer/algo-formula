N = int(input())
A = list(map(int, input().split()))

to = N - 1

while True:
  count = 0

  # バブルソート
  for i in range(to):
    if A[i] > A[i + 1]:
      count += 1
      exchange = A[i]
      A[i]     = A[i + 1]
      A[i + 1] = exchange

  to -= 1

  if count == 0:
    break
  else:
    print(*A)