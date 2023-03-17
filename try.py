N = int(input())

if N == 1:
  print("No")
  exit()

for n in range(2, N):
  if N % n == 0:
    print("No")
    break
else:
  print("Yes")