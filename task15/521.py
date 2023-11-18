for a in range(0, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not (not (x + y - 73 > 0) or not (37 - (x - y) > 0) or (y - a > 0)):
                flag = False
    if flag:
        print(a)
