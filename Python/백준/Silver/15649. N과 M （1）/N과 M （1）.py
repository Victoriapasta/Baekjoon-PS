n, m = map(int, input().split())

visited = [False for i in range(n + 1)]
arr = []


def backTracking():
    global visited
    global arr
    global m

    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        backTracking()
        arr.pop()
        visited[i] = False

backTracking()