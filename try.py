def has_duplicates(list_data):
  return len(list_data) != len(set(list_data))

N = int(input())

strs = [input() for _ in range(N)]

print("Yes" if has_duplicates(strs) else "No")