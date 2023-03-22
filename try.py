N = int(input())

for n in range(1, N + 1):
  if (n % 4 == 0) and (n % 6 == 0):
    print("FizzBuzz")
  elif n % 4 == 0:
    print("Fizz")
  elif n % 6 == 0:
    print("Buzz")
  else:
    print(n)