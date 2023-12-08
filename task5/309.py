def f(n):
    s_n = str(n)
    st1 = ''
    for d in s_n:
        b_d = f'{int(d):0>4b}'
        st1 += b_d + str(b_d.count('1') % 2)
    st2 = '1' + st1[2:] + '0'
    return int(st2, 2)


for i in range(1000, 10000):
    if f(i) == 674890:
        print(i)
        break