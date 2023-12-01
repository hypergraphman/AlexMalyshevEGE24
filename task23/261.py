def f(x):
    if x == 22 or x < 2:
        return 0
    if x == 2:
        return 1
    return f(x - 2) + f(x // 2) + f(x // 3)


print(f(40))