x = int(input())
y = int(input())
z = int(input())

s = str(x * y * z)
counts = [0] * 10

for c in s:
    i = int(c)
    counts[i] += 1

for x in counts:
    print(x)
