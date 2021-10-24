# https://www.acmicpc.net/problem/2442

def printOneLine(stars, length):
    indent = (length - stars) // 2
    print(' ' * indent + '*' * stars + ' ' * indent)


n = int(input())
for i in range(1, n + 1):
    printOneLine(i * 2 - 1, n * 2 - 1)
