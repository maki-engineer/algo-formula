from collections import deque

N = int(input())
A = list(map(int, input().split()))

def merge_sort(ary):
  if len(ary) == 0:
    return

  X    = round(len(ary) / 2)
  L, R = ary[:X], ary[X:]

  if len(L) >= 2:
    L = merge_sort(L)
  if len(R) >= 2:
    R = merge_sort(R)

  dq = deque()

  for l in L:
    dq.append(l)
  for r in reversed(R):
    dq.append(r)

  B = []

  while len(dq):
    if dq[0] <= dq[-1]:
      B.append(dq.popleft())
    else:
      B.append(dq.pop())

  return B

A = merge_sort(A)

print(*A)