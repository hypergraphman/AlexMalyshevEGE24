line = open('24-264.txt').read()
cur_len = 1
max_len = 1
for p1, p2 in zip(line, line[1:]):
    if p1.isdigit() != p2.isdigit():
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)