def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + f(n - 2)


for i in range(1, 50):
    print(i, f(i))