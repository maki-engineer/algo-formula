N    = int(input())
S, T = input(), input()

count = 0

for n in range(N):
  if S[n] != T[n]:
    count += 1

print(count)