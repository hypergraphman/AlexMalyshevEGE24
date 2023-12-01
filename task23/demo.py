def f(x):
    if x == 11 or x > 20:
        return 0
    if x == 20:
        return 1
    return f(x + 1) + f(x * 2) + f(x ** 2)


print(f(2))