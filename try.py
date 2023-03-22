sa, ta = map(int, input().split())
sb, tb = map(int, input().split())

count = 0

from_time, to_time = min(sa, ta, sb, tb), max(sa, ta, sb, tb)

for time in range(from_time, to_time + 1):
  if (sa <= time) and (sb <= time) and (ta > time) and (tb > time): count += 1

print(count)