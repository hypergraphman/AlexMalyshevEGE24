def f(n):
    if n <= 5:
        return n
    if n % 4 == 0:
        return n + f(n / 2 - 1)
    return n + f(n + 2)


for i in range(10000, 1, -1):
    try:
        f(i)
        print(i)
    except:
        pass