u1, u2, u3, u4 = 15, 51, 208, 15
s1, s2, s3, s4 = 15, 51, 192, 0

for i in range(1, 32):
    maska = '1' * i + '0' * (32 - i)
    m1, m2, m3, m4 = int(maska[:8], 2), int(maska[8:16], 2), int(maska[16:24], 2), int(maska[24:],2)
    if u1 & m1 == s1 and u2 & m2 == s2 and u3 & m3 == s3 and u4 & m4 == m4:
        print(maska.count('1'))