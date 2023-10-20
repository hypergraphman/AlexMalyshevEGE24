from ipaddress import *
for i in range(1, 32):
    address = str(ip_network(f'15.51.208.15/{i}', False)).split('/')[0]
    if address == '15.51.192.0':
        print(i)