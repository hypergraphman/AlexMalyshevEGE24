from itertools import product, permutations

nums_6 = [''.join(x) for x in permutations('0123456789', r=6) if x[0] != '0']
k = 0
for el in nums_6:
    f = True
    for p1, p2 in zip(el, el[1:]):
        if not (p1 in '02468' and p2 in '13579' or p2 in '02468' and p1 in '13579'):
            f = False
    if f:
        k += 1
print(k)


nums_4 = [''.join(x) for x in product('0123456789', repeat=4) if x[0] != '0']
k = 0
for el in nums_4:
    f = True
    for p1, p2 in zip(el, el[1:]):
        if not (p1 != p2):
            f = False
    if f:
        k += 1
print(k)