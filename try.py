N, M      = map(int, input().split())
menu_list = {}
result    = 0

for n in range(N):
  menu = list(input().split())
  menu_list[menu[0]] = int(menu[1])

orders = list(input().split())

for order in orders:
  result += menu_list[order]

print(result)