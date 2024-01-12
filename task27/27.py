# f = open('27-A_1.txt')
f = open('27-B_1.txt')
n = int(f.readline())
s = 0
mn = float('inf')
for _ in range(n):
    x1, x2 = map(int, f.readline().split())
    s += max(x1, x2)
    if abs(x1 - x2) % 5 != 0 and abs(x1 - x2) < mn:
        mn = abs(x1 - x2)
if s % 5 == 0:
    print(s - mn)
else:
    print(s)
