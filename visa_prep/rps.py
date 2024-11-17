def rps(p1, p2):
    if p1 == p2:
        return "NULL"
    return "Charan" if (p1 == 'R' and p2 == 'P') or (p1 == 'P' and p2 == 'S') or (p1 == 'S' and p2 == 'R') else "Vignesh"
p1, p2 = input().split()
print(rps(p1, p2))
