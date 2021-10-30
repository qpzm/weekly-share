import time
from collections import deque


def main():
    N = int(input())  # 1 ≤ N ≤ 500,000
    # start = time.time()
    # print(solve1(N))
    # end = time.time()
    # print(end - start)

    start = time.time()
    print(solve2(N))
    end = time.time()
    print(end - start)


def solve1(x):
    cards = list(range(1, x + 1))
    while len(cards) != 1:
        cards.pop(0)
        cards.append(cards.pop(0))

    return cards[0]

def solve2(x):
    cards = deque(range(1, x + 1))
    while len(cards) != 1:
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]

main()
