def f(x, end, k, h):
    if x < 1 or k > 7 or (k == 7 and x != end):
        return 0
    if k == 7:
        print(h)
        return 1
    if int(x**0.5) == x**0.5:
        return f(x - 2, end, k + 1, h + f' {1} ') + f(x + 5, end, k + 1, h + f' {2} ') + f(int(x**0.5), end, k + 1, h + f' {3} ')
    else:
        return f(x - 2, end, k + 1, h + f' {1} ') + f(x + 5, end, k + 1, h + f' {2} ')



print(f(28, 3, 0, ''))