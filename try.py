L, R = map(int, input().split())

count = 0

for x in range(L, R + 1):
  for y in range(x + 1, R + 1):
    num_str1, num_str2 = str(x), str(y)

    if num_str1[-1] == num_str2[-1]: count += 1

print(count)