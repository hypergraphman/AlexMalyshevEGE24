# from re import fullmatch
#
# for n in range(133, 10**10, 133):
#     if fullmatch(r'1[02468]2157[13579]*4', str(n)):
#         print(n, n // 133)

# from itertools import product
#
# B = ['']
# for j in range(1, 4):
#     B += [''.join(i) for i in product('13579', repeat=j)]
#
# r = []
# for a in [''.join(i) for i in product('24680', repeat=1)]:
#     for b in B:
#         t = f'1{a}2157{b}4'
#         n = int(t)
#         if n % 133 == 0:
#             r.append(n)
# for e in sorted(r):
#     print(e, e // 133)
#
# 122157574 918478
# 1021575394 7681018
# 1421575554 10688538
# 1821575714 13696058


for n in range(133, 10**10, 133):
    t = str(n)
    a = int(t[1]) % 2 == 0
    b = True
    if len(t) > 7:
        b = all(e in '13579' for e in t[6:-1])
    if len(t) >= 7 and t[0] == '1' and t[-1] == '4' and t[2:6] == '2157' and a and b:
        print(n, n // 133)
