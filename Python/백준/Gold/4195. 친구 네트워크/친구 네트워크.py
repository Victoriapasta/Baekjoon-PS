import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parents[y] = x
        cnt[x] += cnt[y]

    return cnt[x]


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        parents = {}
        cnt = {}

        for i in range(n):
            a, b = map(str, input().split())
            if a not in parents:
                parents[a] = a
                cnt[a] = 1
            if b not in parents:
                parents[b] = b
                cnt[b] = 1
            print(union(a, b))