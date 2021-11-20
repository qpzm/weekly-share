def main():
    N = int(input())
    for _ in range(N):
        print(format(check(str(input()))))

def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif(len(stack) != 0):
            stack.pop()
        else:
            return False

    return len(stack) == 0

def format(x):
    if x:
        return 'YES'
    else:
        return 'NO'


main()
