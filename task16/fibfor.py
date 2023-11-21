n = int(input())
pre = 1
cur = 1
for i in range(3, n + 1):
    cur, pre = pre + cur, cur
print(cur)