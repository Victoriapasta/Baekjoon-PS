import sys
input = sys.stdin.readline
from collections import deque
global dx
dx = [-1, 0, 1, 0]
global dy
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
maps = [[0 for i in range(m)] for j in range(n)]
visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    maps[i] = list(map(int, input().split()))

def bfs():
    que = deque([])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == False:
                que.append((i, j, 0))
                visited[i][j] = True

    while que:
        x, y, dist = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and ny >= 0 and nx < n and ny < m:
                if visited[nx][ny] == False and maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny, dist+1))

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0 and visited[i][j] == False:
                return -1
    return dist

print(bfs())
