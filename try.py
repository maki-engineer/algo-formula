N = int(input())
A = list(map(int, input().split()))

count = 0

for a in A:
  if a > 0:
    count += 1

print(count)