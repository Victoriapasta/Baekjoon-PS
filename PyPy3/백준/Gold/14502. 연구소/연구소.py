import sys
from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

w = 0


def bfs():
    global w
    que = deque()
    second_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if second_graph[i][j] == 2:
                que.append((i, j))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if second_graph[nx][ny] == 0:
                    second_graph[nx][ny] = 2
                    que.append((nx, ny))

    temp = 0

    for i in range(n):
        for j in range(m):
            if second_graph[i][j] == 0:
                temp += 1

    w = max(w, temp)


def backTracking(start):
    if start == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backTracking(start + 1)
                graph[i][j] = 0


backTracking(0)
print(w)
