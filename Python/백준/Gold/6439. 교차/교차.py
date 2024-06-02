import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


def findCross(x1, y1, x2, y2, x3, y3, x4, y4):
    a = ccw(x1, y1, x2, y2, x3, y3)
    b = ccw(x1, y1, x2, y2, x4, y4)
    c = ccw(x3, y3, x4, y4, x1, y1)
    d = ccw(x3, y3, x4, y4, x2, y2)

    if a * b <= 0 and c * d <= 0:
        if x1 < x3 and x1 < x4 and x2 < x3 and x2 < x4:
            return False
        if x3 < x1 and x3 < x2 and x4 < x1 and x4 < x2:
            return False

        if y1 < y3 and y1 < y4 and y2 < y3 and y2 < y4:
            return False
        if y3 < y1 and y3 < y2 and y4 < y1 and y4 < y2:
            return False

        return True

    return False


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        coordinates = list(map(int, input().split()))
        x1, y1, x2, y2, tempx1, tempy1, tempx2, tempy2 = coordinates
        r1 = [min(tempx1, tempx2), min(tempy1, tempy2)]
        r2 = [min(tempx2, tempx1), max(tempy2, tempy1)]
        r3 = [max(tempx1, tempx2), min(tempy2, tempy1)]
        r4 = [max(tempx1, tempx2), max(tempy2, tempy1)]

        if findCross(x1, y1, x2, y2, r1[0], r1[1], r2[0], r2[1]) \
                or findCross(x1, y1, x2, y2, r2[0], r2[1], r4[0], r4[1]) \
                or findCross(x1, y1, x2, y2, r4[0], r4[1], r3[0], r3[1]) \
                or findCross(x1, y1, x2, y2, r3[0], r3[1], r1[0], r1[1]):
            print('T')
        else:
            if r1[0] < x1 < r3[0] and r1[0] < x2 < r3[0] and r1[1] < y1 < r4[1] and r1[1] < y2 < r4[1]:
                print('T')
            else:
                print('F')
