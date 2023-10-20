from ipaddress import *
from itertools import product


def bin_address(ip_address):
    res = ''
    for num in ip_address.split('.'):
        res += f'{int(num):0>8b}'
    return res


net = ip_network('192.168.32.160/255.255.255.240')
bin_net = bin_address(str(net).split('/')[0])[:net.prefixlen]

n = 32 - net.prefixlen
k = 0
for gen in product('01', repeat=n):
    bin_a = bin_net + ''.join(gen)
    if bin_a.count('1') % 2 == 0:
        k += 1
print(k)
