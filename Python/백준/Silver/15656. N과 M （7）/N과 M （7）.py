import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))
outputArr = []


def backTracking():
    global arr
    global m
    global outputArr

    if len(outputArr) == m:
        print(*outputArr)
        return

    for i in range(len(arr)):

        outputArr.append(arr[i])
        backTracking()
        outputArr.pop()


backTracking()