import sys
from math import sqrt

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = parents[x]
    else:
        parents[x] = parents[y]


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        parents = [i for i in range(n)]
        arr = []
        for __ in range(n):
            arr.append(list(map(int, input().split())))

        for i in range(n - 1):
            for j in range(i, n):
                x1, y1, r1 = arr[i]
                x2, y2, r2 = arr[j]
                if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1 + r2:
                    union(i, j)

        group = set()
        for i in range(n):
            if find(i) not in group:
                group.add(i)

        print(len(group))