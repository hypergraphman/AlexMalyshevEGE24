from string import digits, ascii_uppercase


def n_to_p(n, p):
    alph = digits + ascii_uppercase
    res = ''
    while n > 0:
        digit = alph[n % p]
        res = digit + res
        n //= p
    return res


# print(n_to_p(255, 16))
# print(n_to_p(194, 5))


def f(n):
    s1 = n_to_p(n, 3)
    if n % 3 == 0:
        s2 = '1' + s1 + '02'
    else:
        s2 = s1 + n_to_p(n % 3 * 4, 3)
    return int(s2, 3)


# print(f(11))
# print(f(12))

for i in range(1, 200):
    if f(i) < 199:
        print(i)