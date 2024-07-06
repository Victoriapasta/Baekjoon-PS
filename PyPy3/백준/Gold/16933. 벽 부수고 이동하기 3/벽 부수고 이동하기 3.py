import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n, m, k = map(int, input().split())
graph = []
visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input().rstrip())))


def bfs():
    global dx
    global dy
    global visited
    que = deque([(0, 0, 0, 1)])

    while que:
        x, y, w, day = que.popleft()

        if x == n - 1 and y == m - 1:
            return day

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[w][nx][ny] == 0:  # 값이 0이면 방문을 안 했다는 뜻
                    visited[w][nx][ny] = day
                    que.append((nx, ny, w, day + 1))

                if graph[nx][ny] == 1 and w < k and visited[w + 1][nx][ny] == 0:
                    if day % 2 == 1:
                        visited[w + 1][nx][ny] = day
                        que.append((nx, ny, w + 1, day + 1))
                    else:
                        que.append((x, y, w, day + 1))

    return -1


print(bfs())
