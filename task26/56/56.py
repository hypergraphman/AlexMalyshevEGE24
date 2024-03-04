f = open('26.txt')
v, d, _ = map(int, f.readline().split())
files = sorted(map(int, f))
disks = [v] * d
fail_files = []
while files:
    file = files.pop()
    j = 0
    for i in range(len(disks)):
        if disks[(i + j) % d] >= file:
            disks[(i + j) % d] -= file
            j = i
            break
    else:
        fail_files.append(file)
print(sum(fail_files), len(fail_files))
