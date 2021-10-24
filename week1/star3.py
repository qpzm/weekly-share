# https://www.acmicpc.net/problem/2522

n = int(input())
for i in range(1, 2 * n):
    indent = abs(i - n)
    print(' ' * indent + '*' * (n - indent))
