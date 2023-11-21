import time
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + f(n - 2)


start = time.time()
for i in range(1, 50):
    print(i, f(i), time.time() - start)
    start = time.time()