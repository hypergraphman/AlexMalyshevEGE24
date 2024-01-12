lines = open('24.txt').read().split('A')
a = [len(line) for line in lines if line.count('E') >= 3]
print(max(a))