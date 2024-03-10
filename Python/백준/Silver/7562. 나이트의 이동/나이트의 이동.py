import sys
from collections import deque

input = sys.stdin.readline

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

n = int(input())


def bfs(startX, startY, visited, graph, length):
    que = deque(())
    que.append((startX, startY, 0))
    while que:
        x, y, distance = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    return distance + 1

                visited[nx][ny] = True
                que.append((nx, ny, distance + 1))


for i in range(n):
    length = int(input())

    graph = [[0 for __ in range(length)] for _ in range(length)]
    visited = [[False for __ in range(length)] for _ in range(length)]

    nowX, nowY = map(int, input().split())
    destinationX, destinationY = map(int, input().split())

    graph[destinationX][destinationY] = 1

    if nowX == destinationX and nowY == destinationY:
        print(0)
    else:
        print(bfs(nowX, nowY, visited, graph, length))
