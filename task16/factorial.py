# n = 5
# f = 1
# for i in range(1, 6):
#     f *= i
# print(f)


def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n


print(f(5))