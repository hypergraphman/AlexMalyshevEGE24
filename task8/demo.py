from itertools import permutations

count = 0
a = [''.join(x) for x in permutations('0234567', r=5)]
for x in a:
    if x[0] != '0':
        x = x.replace('4', '2').replace('6', '2').replace('0', '2').replace('5', '3').replace('7', '3')
        if '22' not in x and '33' not in x:
            count += 1
print(count)
print(3 * 4 * 2 * 3 + 3 * 3 * 3 * 2 * 2)