from functools import lru_cache


@lru_cache(None)
def F(n):
    if n > 2074:
        return n
    if n <= 2074:
        return n + F(n + 1) + F(n + 2)


for i in range(2074, 1, -500):
    try:
        F(i)
    except Exception:
        pass


print(F(22) // F(24))