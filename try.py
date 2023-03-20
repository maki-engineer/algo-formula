N = int(input())
S = input()

results = [(x, y) for x in range(N) for y in range(x + 1, N) if S[x] == S[y]]
print(len(results))