S = input()

count  = 0
string = ""

for s in S:
  if string == s:
    count += 1
  else:
    string = s

print(count)