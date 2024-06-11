x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

maxx1, maxx2, minx1, minx2 = max(x1, x2), max(x3, x4), min(x1, x2), min(x3, x4)
maxy1, maxy2, miny1, miny2 = max(y1, y2), max(y3, y4), min(y1, y2), min(y3, y4)


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


a = ccw(x1, y1, x2, y2, x3, y3)
b = ccw(x1, y1, x2, y2, x4, y4)
c = ccw(x3, y3, x4, y4, x1, y1)
d = ccw(x3, y3, x4, y4, x2, y2)

if a * b == 0 and c * d == 0:
    if minx1 <= maxx2 and minx2 <= maxx1 and miny1 <= maxy2 and miny2 <= maxy1:
        print(1)
        exit(0)
else:
    if a * b < 0 and c * d < 0:
        print(1)
        exit(0)

print(0)
