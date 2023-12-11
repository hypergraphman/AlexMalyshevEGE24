from collections import defaultdict, Counter

L = []
for s in open('24-164.txt'):
    D = defaultdict(int)
    for i in range(len(s) - 1):
        if s[i] == 'X':
            D[s[i + 1]] += 1
    M = max(D.values())
    L.extend([c for c in D if D[c] == M])

print(Counter(L))
