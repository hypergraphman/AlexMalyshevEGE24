from time import time

cur_time = time()
line = open('24-271.txt').read()
a = list(filter(lambda y: len(y) == 6, map(lambda x: x[:6], line.split('#'))))

k = 0
for el in a:
    try:
        k += int(el[2:4], 16) < int(el[0:2], 16) > int(el[4:], 16)
    except:
        pass
print(k, time() - cur_time)