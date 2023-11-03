from string import digits, ascii_uppercase


def n_to_p(n, p):
    alph = digits + ascii_uppercase
    res = ''
    while n > 0:
        digit = alph[n % p]
        res = digit + res
        n //= p
    return res


def f(n):
    s1 = n_to_p(n, 5)
    if n % 5 == 0:
        s2 = s1 + s1[-2:]
    else:
        s2 = s1 + n_to_p(n % 5 * 7, 5)
    return int(s2, 5)


a = []
for i in range(5, 200):
    if f(i) > 200:
        a.append(f(i))
print(min(a))