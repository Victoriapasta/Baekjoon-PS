import sys
input = sys.stdin.readline
from collections import deque
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]
visited = [[[False for __ in range(m)] for _ in range(n)] for ___ in range(h)]
for _ in range(h):
    for __ in range(n):
        graph[_].append(list(map(int, input().split())))
cnt = 0
que = deque([])

def bfs():

    while que:
        x, y, z, dist = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if n > nx >= 0 and m > ny >= 0 and h > nz >= 0 and not visited[nz][nx][ny] and graph[nz][nx][ny] != -1:
                visited[nz][nx][ny] = True
                que.append((nx, ny, nz, dist+1))

    return dist

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1 and not visited[k][i][j]:
                que.append((i, j, k, 0))
                visited[k][i][j] = True
if que:
    cnt = bfs()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0 and not visited[k][i][j]:
                print(-1)
                exit(0)
print(cnt)