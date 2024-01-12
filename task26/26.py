f = open('26.txt')
v, n = map(int, f.readline().split())
a = sorted([int(x) for x in f])
k = 0
s = 0
while s + a[k] <= v:
    s += a[k]
    k += 1
print(k, s, v)
s -= a[k - 1]
t = v - s
print(t)
mx = 0
for el in a:
    if el > mx and el <= t:
        mx = el
print(mx)