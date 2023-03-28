N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
  pos = i

  # posが0になるまで昇順の入れ替え作業
  while pos != 0:

    if A[pos] < A[pos - 1]:
      exchange   = A[pos]
      A[pos]     = A[pos - 1]
      A[pos - 1] = exchange

    pos -= 1

  print(*A)