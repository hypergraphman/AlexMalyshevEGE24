for a in 0, 1:
    for b in 0, 1:
        f1 = a and b and not a and b or b
        f2 = b
        print(f1, f2)