from itertools import product

nums = [''.join(x) for x in product('01234567', repeat=6) if x[0] != '0' and x.count('6') == 2]
k = 0
for n in nums:
    if not('16' in n or '36' in n or '56' in n or '76' in n or '61' in n or '63' in n or '65' in n or '67' in n):
        k += 1
print(k)