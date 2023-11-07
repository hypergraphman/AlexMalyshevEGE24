for a in range(0, 200):
    is_a = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x + 2 * y < a) or (y > x) or (x > 60)):
                is_a = False
    if is_a:
        print(a)
        break
