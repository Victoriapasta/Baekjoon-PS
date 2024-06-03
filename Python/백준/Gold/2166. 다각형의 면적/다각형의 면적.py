import sys

input = sys.stdin.readline


def getWidth(list):
    list.append(list[0])
    positive = 0
    negative = 0
    for i in range(len(list) - 1):
        positive += list[i][0] * list[i + 1][1]
        negative += list[i][1] * list[i + 1][0]

    return round(abs(positive - negative) / 2, 1)


if __name__ == '__main__':
    n = int(input())
    pos = []
    for _ in range(n):
        pos.append(list(map(int, input().split())))

    print(getWidth(pos))