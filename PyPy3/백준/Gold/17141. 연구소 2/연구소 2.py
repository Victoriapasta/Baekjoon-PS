import sys
from collections import deque

INF = int(10 ** 9)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

result = INF


def bfs():
    global result
    visited = [[0] * n for _ in range(n)]
    que = deque()
    dist = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:  # -1이 바이러스를 놓은 자리
                visited[i][j] = 1
                que.append((i, j))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
                    dist = max(dist, visited[nx][ny]) - 1

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not graph[i][j] == 1:
                return INF

    return dist


def backTracking(N, M):
    global result
    if M == m:
        result = min(result, bfs())
        return

    for _ in range(N, n * n):
        i, j = _ // n, _ % n
        if graph[i][j] == 2:
            graph[i][j] = -1
            backTracking(_, M + 1)
            graph[i][j] = 2


backTracking(0, 0)
if result == INF:
    print(-1)
else:
    print(result)