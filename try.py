N, V = map(int, input().split())
A    = list(map(int, input().split()))

for a in A:
  if a == V:
    print("Yes")
    break
else:
  print("No")