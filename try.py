N = int(input())
A = list(map(int, input().split()))

count = 0

def check_prime_number(num):
  check_not_prime = False

  if num == 1:
    return True

  for n in range(2, num):
    if num % n == 0:
      check_not_prime = True
      break

  return check_not_prime

for a in A:
  if not check_prime_number(a):
    count += 1

print(count)