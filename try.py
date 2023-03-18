S = input()

data      = []
check_str = ''

for s in S:
  if check_str != s:
    if not s in data:
      check_str = s
      data.append(check_str)

print(len(data))