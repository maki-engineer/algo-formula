S = input()

str_index = len(S) - 1
to         = len(S) // 2

for i in range(to):
  if S[i] != S[str_index - i]:
    print("No")
    break
else:
  print("Yes")