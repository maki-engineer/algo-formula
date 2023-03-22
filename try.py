ans = 0
for i in range(30):
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == M1 == H2 == M2 == 0:
        continue
    m = 60 * (H2 - H1) + M2 - M1
    if 360 < m <= 480:
        m -= 45
    elif m > 480:
        m -= 60
    ans += m
print(ans // 60, ans % 60)