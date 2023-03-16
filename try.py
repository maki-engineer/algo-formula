N = int(input())
A = list(map(int, input().split()))

max_num   = 0
max_index = -1

for i in range(N):
  if A[i] > max_num:
    max_num   = A[i]
    max_index = i

print(max_index)