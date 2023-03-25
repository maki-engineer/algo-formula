N = int(input())
A = list(map(int, input().split()))

max_num   = 0
duplicate = 0

for i in range(len(A)):
  if i == 0:
    max_num   = A[i]
    duplicate = 1
    print(duplicate)
    continue

  if max_num == A[i]:
    duplicate += 1
    print(duplicate)
  elif max_num < A[i]:
    max_num = A[i]
    duplicate = 1
    print(duplicate)
  else:
    print(duplicate)