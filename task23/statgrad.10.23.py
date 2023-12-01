def f(x, e):
    if x == 12 or x > e:
        return 0
    if x == e:
        return 1
    return f(x + 1, e) + f(x * 2, e) + f(x ** 2, e)


print(f(3, 10) * f(10, 25))