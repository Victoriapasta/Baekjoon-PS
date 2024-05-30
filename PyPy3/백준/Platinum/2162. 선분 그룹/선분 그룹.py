import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


def findCross(list1, list2):
    x1, y1, x2, y2 = list1
    x3, y3, x4, y4 = list2

    maxx1, maxx2, minx1, minx2 = max(x1, x2), max(x3, x4), min(x1, x2), min(x3, x4)
    maxy1, maxy2, miny1, miny2 = max(y1, y2), max(y3, y4), min(y1, y2), min(y3, y4)

    a = ccw(x1, y1, x2, y2, x3, y3)
    b = ccw(x1, y1, x2, y2, x4, y4)
    c = ccw(x3, y3, x4, y4, x1, y1)
    d = ccw(x3, y3, x4, y4, x2, y2)

    if a * b == 0 and c * d == 0:
        if minx1 <= maxx2 and minx2 <= maxx1 and miny1 <= maxy2 and miny2 <= maxy1:
            return True
    else:
        if a * b <= 0 and c * d <= 0:
            return True

    return False


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[x] = y
    else:
        parents[y] = x


if __name__ == '__main__':
    n = int(input())

    coordinates = []
    for i in range(n):
        coordinates.append(list(map(int, input().split())))

    parents = [i for i in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if findCross(coordinates[i], coordinates[j]):
                union(i, j)

    cnt = 0
    group = [0 for _ in range(n)]

    for i in range(n):
        if parents[i] == i:
            cnt += 1

        group[find(i)] += 1

    print(cnt)
    print(max(group))