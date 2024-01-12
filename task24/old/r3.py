s = open('7k.txt').read()
temp = 'EAB'
k = 0
m = 0
i_m = -1
for i in range(len(s)):
    if s[i] == temp[k % len(temp)]:
        k += 1
        if k > m:
            m = k
            i_m = i
    else:
        if s[i] == temp[0]:
            k = 1
        else:
            k = 0
print(s[i_m - m + 1:i_m + 1])