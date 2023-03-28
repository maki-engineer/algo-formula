N = int(input())
A = list(map(int, input().split()))

half_index = N // 2
L, R       = [], []

for i in range(N):
  # Lに代入
  if (A[half_index] > A[i]) and (half_index != i):
    L.append(A[i])

  # Rに代入
  if (A[half_index] <= A[i]) and (half_index != i):
    R.append(A[i])

# LとRをそれぞれ昇順にソート
L = sorted(L)
R = sorted(R)

print(*L, A[half_index], *R)