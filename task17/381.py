f = open('17-381.txt')
a = [int(x) for x in f]
# a = list(map(int, f))

# mx = -float('inf')
# for el in a:
#     if len(str(abs(el))) == 4 and abs(el) % 100 == 39 and el > mx:
#         mx = el

mx = max(filter(lambda el: len(str(abs(el))) == 4 and abs(el) % 100 == 39, a))

b = []
for p1, p2 in zip(a, a[1:]):
    if ((len(str(abs(p1))) == 4) != (len(str(abs(p2))) == 4) and
       (p1 + p2) ** 2 <= mx ** 2):
        b.append(p1 + p2)
print(len(b), max(b))

# c = 0
# mx_d = -float('inf')
# for i in range(len(a) - 1):
#     p1, p2 = a[i], a[i + 1]
#     if (1000 <= abs(p1) <= 9999) + (1000 <= abs(p2) <= 9999) == 1 and (p1 + p2) ** 2 <= mx ** 2:
#         c += 1
#         if p1 + p2 > mx_d:
#             mx_d = p1 + p2
# print(c, mx_d)