n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))
visited = [False] * (n + 1)
temp = []


def backTracking(start):
    global arr
    global m
    global temp

    recur = 0
    if len(temp) == m:
        print(*temp)
        return

    for i in range(start, len(arr)):
        if visited[i] or recur == arr[i]:
            continue
        temp.append(arr[i])
        recur = arr[i]
        visited[i] = True
        backTracking(i+1)
        temp.pop()
        visited[i] = False


backTracking(0)
