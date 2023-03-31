import random

N = int(input())
A = list(map(int, input().split()))

def quick_sort(ary):
  # 配列が空の場合は空配列を返す
  if not ary:
    return []

  half_index = random.randrange(len(ary))
  L, R       = [], []

  # ソート
  for i, value in enumerate(ary):
    if i == half_index: continue

    if value == ary[half_index]:
      if random.randrange(2):
        L.append(value)
      else:
        R.append(value)
    elif value < ary[half_index]:
      L.append(value)
    else:
      R.append(value)

  # L, Rを再帰的にソートする
  L = quick_sort(L)
  R = quick_sort(R)

  # Lをつなげていく
  L.append(ary[half_index])
  L.extend(R)

  return L

A = quick_sort(A)

print(*A)