for a in range(0, 200):
    if all([(x + 2 * y < a) or (y > x) or (x > 60) for x in range(0, 100) for y in range(0, 100)]):
        print(a)
        break