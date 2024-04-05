import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n, m, k = map(int, input().split())
graph = []
visited = [[[0] * (m) for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input().rstrip())))


def bfs():
    global dx
    global dy
    que = deque([(0, 0, 0)])

    while que:
        x, y, w = que.popleft()

        if x == n - 1 and y == m - 1:
            return visited[w][x][y]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[w][nx][ny] == 0:  # 값이 0이면 방문을 안 했다는 뜻
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    que.append((nx, ny, w))
                    continue

                if graph[nx][ny] == 1 and w < k and visited[w + 1][nx][ny] == 0:
                    visited[w + 1][nx][ny] = visited[w][x][y] + 1
                    que.append((nx, ny, w + 1))
                    continue

    return -1


print(bfs())
