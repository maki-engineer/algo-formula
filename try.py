N = int(input())
A = list(map(int, input().split()))

max_num = -101

for a in A:
  if max_num < a:
    max_num = a

print(max_num)