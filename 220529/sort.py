def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

# print(l)
for i in range(N):
    maxIndex = 0
    for j in range(1, N - i):
        if l[maxIndex] < l[j]:
            maxIndex = j
    swap(l, maxIndex, N-i-1)

for i in range(N):
    print(l[i])
