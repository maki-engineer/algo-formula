H, W, p, q = map(int, input().split())

print("Black" if (p + q) % 2 == 0 else "White")