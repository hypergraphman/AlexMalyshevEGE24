from collections import defaultdict, Counter

letters = []
letters1 = []
for s in open('24-164.txt').readlines():
    if 'X' in s:  # and (s[-1] != 'X' or s.count('X') > 1):
        d = defaultdict(int)
        for c1, c2 in zip(s, s[1:]):
            if c1 == 'X':
                d[c2] += 1
        d_r = defaultdict(list)
        for k, v in d.items():
            d_r[v] += [k]
        letters += sorted(d_r.items())[::-1][0][1]
print(Counter(letters))