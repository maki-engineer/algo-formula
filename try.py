N = int(input())
A = list(map(int, input().split()))

# まずは最高値を求める
max_num = max(A)

# 最高値のインデックスを求める
max_num_index = A.index(max_num)

check = 0

for i in range(len(A)):
  if i == max_num_index: continue

  if check < A[i]: check = A[i]

print(check)