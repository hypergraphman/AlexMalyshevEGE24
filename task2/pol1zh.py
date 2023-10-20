from itertools import product

for a, b, c in product((0, 1), repeat=3):
    f = int(not (a and c) or not (b and not c))
    print(a, b, c, f)