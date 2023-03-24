N, M   = map(int, input().split())
result = N

while N > 0:
  if N >= M:
    N      -= M
    N      += 1
    result += 1
  else:
    N = 0

print(result)