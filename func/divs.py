def divs(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


def is_prime(n):
    return len(divs(n)) == 2


for i, n in enumerate(range(245690, 245756), start=1):
    if is_prime(n):
        print(i, n)
