from re import fullmatch


def divs(n):
    res = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
    return sorted(res)


def is_prime(n):
    return len(divs(n)) == 2


primes = []
for i in range(2, 160):
    if is_prime(i):
        primes.append(i)


for n in range(100, 10000 + 1):
    t = n
    i = 0
    k = 0
    last_i = primes[i]
    while t > 1 and i < len(primes):
        if t % primes[i] == 0:
            k += 1
            t //= primes[i]
            last_i = primes[i]
        else:
            i += 1
    if k == 7 and fullmatch(r'\d*2\d2', str(n)):
        print(n, last_i)