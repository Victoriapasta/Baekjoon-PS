n, m = map(int, input().split())

arr = []


def backTracking(start):
    global visited
    global arr
    global m

    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n + 1):
        arr.append(i)
        backTracking(i)
        arr.pop()


backTracking(1)
