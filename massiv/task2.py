n = int(input())
p1 = int(input())
sp2 = []
for _ in range(n - 1):
    p2 = int(input())
    sp2.append(p1 + p2)
    p1 = p2

print(sp2)
