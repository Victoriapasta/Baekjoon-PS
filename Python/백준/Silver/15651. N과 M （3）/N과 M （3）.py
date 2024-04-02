n, m = map(int, input().split())

arr = []


def backTracking():
    global visited
    global arr
    global m

    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr.append(i)
        backTracking()
        arr.pop()

backTracking()