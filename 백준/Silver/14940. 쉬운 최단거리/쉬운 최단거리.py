import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

graph = []
visited = [[False for _ in range(m)] for __ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(startx, starty):
    que = deque([(startx, starty, 0)])
    graph[startx][starty] = 0
    visited[startx][starty] = True

    while que:
        x, y, dist = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if n > nx >= 0 and m > ny >= 0 and not visited[nx][ny] and graph[nx][ny] != 0:
                que.append((nx, ny, dist+1))
                visited[nx][ny] = True
                graph[nx][ny] = dist+1

temp = 0
for i in range(n):
    if temp:
        break
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            temp = 1
            break

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            graph[i][j] = -1
            visited[i][j] = True

for i in range(n):
    print(*graph[i])
