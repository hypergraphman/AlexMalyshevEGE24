a = [123, 231, 1234]

min_digit = float('inf')
for el in a:
    min_digit = min(min_digit, sum(map(int, str(el))))

b = list(filter(lambda x: sum(map(int, str(x))) == min_digit, a))

print(max(b))