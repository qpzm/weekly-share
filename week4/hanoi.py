def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1

def move_hanoi(n, src, via, dest):
    if n == 1:
        print(f'{src} {dest}')
    else:
        move_hanoi(n - 1, src, dest, via)
        print(f'{src} {dest}')
        move_hanoi(n - 1, via, src, dest)

N = int(input())
print(hanoi(N))
move_hanoi(N, 1, 2, 3)
