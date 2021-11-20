# F_0 = 0, F_1 = 1
# Top-down
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


# Bottom-up
def fibo2(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b

    return a


N = int(input())
print(fibo2(N))
print(fibo(N))
