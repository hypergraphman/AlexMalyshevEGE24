from time import time

f = open('24_2024.txt')
cur_time = time()
a = list(map(len, f.read().split('T')))
print(time() - cur_time)
k = 100
cur_time = time()
mx = 0
for i in range(len(a) - k):
    s = sum(a[i:i + k + 1])
    mx = max(s, mx)
print(time() - cur_time)
print(mx + k)