def d(st):
    s = sum(map(int, st))
    if sum(map(int, st)) % 2 == 0:
        return '11' + st[2:] + '00'
    else:
        return '10' + st[2:] + '11'


def f(n):
    st1 = f'{n:b}'
    st2 = d(st1)
    st3 = d(st2)
    return int(st3, 2)


a = []
for i in range(1, 1500):
    if f(i) < 1500:
        a.append(f(i))
print(max(a))