f = open('26.txt')
n, s = map(int, f.readline().split())

a = sorted([int(x) for x in f], reverse=True)

reis = 0
while a:
    i = 0
    m = s
    while i < len(a):
        if m - a[i] >= 0:
            m -= a.pop(i)
        else:
            i += 1
    reis += 1
print(reis, s - m)

