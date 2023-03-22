N = int(input())

check = False

if N % 4 == 0:
  check = True

  if N % 100 == 0:
    check = False

    if N % 400 == 0:
      check = True

print("Yes" if check else "No")