for a in range(1, 200):
    if all([((x % 2 == 0) <= (not (x % 3 == 0))) or (x + a >= 100) for x in range(1, 100)]):
        print(a)
        break
