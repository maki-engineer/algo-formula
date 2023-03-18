N = int(input())

count = 0

# 回文数を調べる関数
def check_palindrome(string):
  is_palindrome = True
  half_index    = len(string) // 2
  to_index      = len(string) - 1

  for s in range(half_index):
    if string[s] != string[to_index - s]:
      is_palindrome = False
      break

  return is_palindrome

for _ in range(N):
  check_str = input()

  if check_palindrome(check_str):
    count += 1

print(count)