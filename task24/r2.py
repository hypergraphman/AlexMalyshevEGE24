s = open('7k.txt').read().replace('D', 'E').split('E')
print(max(map(len, s)))

