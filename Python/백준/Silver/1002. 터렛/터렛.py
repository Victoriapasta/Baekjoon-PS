import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if not dist:
        if r1 == r2:
            print(-1)
            continue
        print(0)
        continue
    if dist:
        if r1 + r2 == dist or abs(r2 - r1) == dist:
            print(1)
            continue
        if abs(r2 - r1) < dist < r1 + r2:
            print(2)
            continue
        print(0)
