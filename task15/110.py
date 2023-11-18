u = set(range(1, 100))
p = set(range(2, 21, 2))
q = set(range(5, 51, 5))
a = set()
for n in u:
    if ((u - {n}) | p) & ((u - {n}) | (u - q)) == u:
        a.add(n)
print(a)
