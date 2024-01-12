# for i in range(101):
f = open(f'7k.txt')
s = f.read()
f.close()
k = 0
m = 0
i_m = -1
for i in range(len(s)):
    if s[i] in 'ABC':
        k += 1
        if k > m:
            m = k
            i_m = i
    else:
        k = 0
print(s[i_m - m + 1:i_m + 1])
