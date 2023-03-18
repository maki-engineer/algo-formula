L, R = map(int, input().split())

count = 0

# 回文数か調べる関数
def check_palindrome(num):
  is_palindrome = True
  str_num       = str(num)
  str_index     = len(str_num) // 2
  to_index      = len(str_num) - 1

  for n in range(str_index):
    if str_num[n] != str_num[to_index - n]:
      is_palindrome = False
      break

  return is_palindrome

for num in range(L, R + 1):
  if check_palindrome(num):
    count += 1

print(count)