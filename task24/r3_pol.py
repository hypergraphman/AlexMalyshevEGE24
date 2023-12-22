with open("7k.txt", "r") as F:
    s = F.readline()
k = ''
while k in s:
    k += 'E'
    if k in s:
        k += 'A'
        if k in s:
            k += 'B'
print(len(k) - 1)
print(k)
