N = int(input())
A = list(map(int, input().split()))

for j in range(N - 1):
  # 最小値と最小値の場所の変数
  min_num   = 1001
  min_index = N + 1

  # 最小値探索
  for k in range(j, N):
    if min_num > A[k]:
      min_num   = A[k]
      min_index = k

  # 交換
  exchange     = A[j]
  A[j]         = A[min_index]
  A[min_index] = exchange

  #出力
  print(*A)