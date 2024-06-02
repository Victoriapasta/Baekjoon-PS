import sys
import math

input = sys.stdin.readline


def calcDistance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def findHome(facility):
    answerx, answery = 0, 0
    minn = float(10 ** 9)
    for x1, y1, in facility:
        maxx = 0
        for x2, y2 in facility:
            temp = calcDistance(x1, x2, y1, y2)
            if temp > maxx:
                maxx = temp
        if minn > maxx:
            minn = maxx
            answerx, answery = x1, y1

    print(answerx, answery)


if __name__ == '__main__':
    n = int(input())
    facilities = []
    for _ in range(n):
        facilities.append(list(map(float, input().split())))

    findHome(facilities)
