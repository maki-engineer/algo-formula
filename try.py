N = int(input())
A = list(map(int, input().split()))

min_num = 101

for a in A:
  if a < min_num:
    min_num = a

print(min_num)