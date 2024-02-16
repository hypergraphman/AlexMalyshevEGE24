f = open('26.txt')
n, s = map(int, f.readline().split())
a = []
for line in f.readlines():
    t, c, k = line.split()
    if t == 'Z':
        s -= int(c) * int(k)
    else:
        a.append((int(c), int(k)))
print(s)
a.sort(key=lambda x: x[0])
count = 0
for c, k in a:
    if s - c * k >= 0:
        s -= c * k
        count += k
    else:
        count += s // c
        s %= c
        break
print(count, s)
