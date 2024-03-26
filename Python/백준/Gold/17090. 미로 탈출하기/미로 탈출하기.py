import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
graph = []
for i in range(n):
    st = input()
    graph.append(st[:-1])

memoization = [[False for i in range(m)] for j in range(n)]
visited = [[False for i in range(m)] for j in range(n)]


def dfs(start_x, start_y):
    global graph
    global memoization
    global visited

    if visited[start_x][start_y]:
        return memoization[start_x][start_y]

    if memoization[start_x][start_y]:
        return True

    visited[start_x][start_y] = True

    if graph[start_x][start_y] == 'U':
        next_x, next_y = start_x - 1, start_y
        if 0 > next_x or 0 > next_y or next_x >= n or next_y >= m:
            memoization[start_x][start_y] = True
        elif dfs(next_x, next_y):
            memoization[start_x][start_y] = True

    if graph[start_x][start_y] == 'R':
        next_x, next_y = start_x, start_y + 1
        if 0 > next_x or 0 > next_y or next_x >= n or next_y >= m:
            memoization[start_x][start_y] = True
        elif dfs(next_x, next_y):
            memoization[start_x][start_y] = True

    if graph[start_x][start_y] == 'D':
        next_x, next_y = start_x + 1, start_y
        if 0 > next_x or 0 > next_y or next_x >= n or next_y >= m:
            memoization[start_x][start_y] = True
        elif dfs(next_x, next_y):
            memoization[start_x][start_y] = True

    if graph[start_x][start_y] == 'L':
        next_x, next_y = start_x, start_y - 1
        if 0 > next_x or 0 > next_y or next_x >= n or next_y >= m:
            memoization[start_x][start_y] = True
        elif dfs(next_x, next_y):
            memoization[start_x][start_y] = True

    return memoization[start_x][start_y]

answer = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)

