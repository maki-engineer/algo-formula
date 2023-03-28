from random import randint

N = int(input())
A = list(map(int, input().split()))

rand_index = randint(0, N - 1)
L, R       = [], []

for i in range(N):
  # rand_index == i なら飛ばす
  if rand_index == i: continue

  # Lに代入
  if A[rand_index] > A[i]:
    L.append(A[i])

  # Rに代入
  if A[rand_index] <= A[i]:
    R.append(A[i])

# LとRをそれぞれ昇順にソート
L = sorted(L)
R = sorted(R)

print(*L, A[rand_index], *R)