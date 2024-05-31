import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    parents = [i for i in range(n)]

    for i in range(n):
        link = list(map(int, input().split()))
        for j in range(n):
            if link[j]:
                union(i, j)

    dist = list(map(int, input().split()))
    parents = [-1] + parents
    start = parents[dist[0]]
    for i in range(1, m):
        if parents[dist[i]] != start:
            print('NO')
            exit(0)
    print('YES')
