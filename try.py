nums = list(map(int, input().split("/")))

for n in range(2, max(nums[0], nums[1]) + 1):
  # 約分
  if (nums[0] % n == 0) and (nums[1] % n == 0):
    nums[0] = nums[0] // n
    nums[1] = nums[1] // n
    n = 2

# 文字列に変換して結果を出力
print("/".join(list(map(str, nums))))