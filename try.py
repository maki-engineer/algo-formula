N = int(input())
A = list(map(int, input().split()))

results = [0 for _ in range(9)]

for a in A:
  results[a - 1] += 1

for result in results:
  print(result)