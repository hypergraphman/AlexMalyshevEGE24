from functools import lru_cache


@lru_cache(None)
def f(n):
    st1 = n - f'{n:b}'.count('0')
    st2 = f'{st1:b}'
    st3 = st2[-3:] + st2
    st4 = int(st3, 2)
    return st4


a = []
for i in range(1, 1000):
    if f(i) > 224:
        a.append(f(i))
print(min(a))