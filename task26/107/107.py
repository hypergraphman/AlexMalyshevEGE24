f = open('26-107.txt')
f.readline()
times = []
for line in f:
    times.append(tuple(map(int, line.split())))
times.sort(key=lambda x: (x[1], x[0]))

k = 0
last_start = 0
last_fin = 0
for start, fin in times:
    if start >= last_fin:
        last_fin = fin
        k += 1
        last_start = start
print(k, last_start)