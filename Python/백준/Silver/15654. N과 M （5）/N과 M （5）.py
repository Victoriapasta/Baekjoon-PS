import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (n+1)
outputArr = []


def backTracking():
    global arr

    if len(outputArr) == m:
        print(*outputArr)
        return

    for i in range(len(arr)):
        if visited[i]:
            continue

        outputArr.append(arr[i])
        visited[i] = True
        backTracking()
        outputArr.pop()
        visited[i] = False


backTracking()