N, K = map(int, input().split())

count = 0

# 約数の個数を返す関数
def count_div_num(num):
  count_num = 0

  for n in range(1, num + 1):
    if num % n == 0:
      count_num += 1

  return count_num

for n in range(1, N + 1):
  if count_div_num(n) == K:
    count += 1

print(count)