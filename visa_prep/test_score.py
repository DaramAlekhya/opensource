N, X, Y = map(int, input().split())
print("YES" if Y % X == 0 and Y <= N * X else "NO")
