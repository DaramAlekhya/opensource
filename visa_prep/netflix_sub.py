A,B,C, X =map(int,input().split())
print("YES" if any(a+b>=X for a,b in [(A,B),(A,C),(B,C)]) else "NO")
