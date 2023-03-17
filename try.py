N = int(input())

count = 0

for n in range(1, N + 1):
  if N % n == 0:
    count += 1

print(count)