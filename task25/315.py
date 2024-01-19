from re import fullmatch

for n in range(2025, 10 ** 8, 2025):
    if fullmatch(r'12\d*34\d5', str(n)):
        print(n, n // 2025)

# from itertools import product
#
# a = []
# for x in range(10):
#     for y in [''] + [''.join(i) for i in product('0123456789', repeat=2)] + [''.join(i) for i in product('0123456789', repeat=1)]:
#         t = f'12{y}34{x}5'
#         n = int(t)
#         if n % 2025 == 0:
#             a.append(n)
# for e in sorted(a):
#     print(e, e // 2025)
