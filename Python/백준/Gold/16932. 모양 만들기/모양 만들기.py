import sys
from collections import deque

sys = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for __ in range(n)]


def bfs(startx, starty):
    que = deque([(startx, starty)])
    dist = 1
    visited[startx][starty] = num
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = num
                    dist += 1
                    que.append((nx, ny))

    return dist


num = 2
group = dict()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            group[num] = bfs(i, j)
            num += 1


answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            s = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and visited[nx][ny] not in s:
                        s.add(visited[nx][ny])
            result = 1

            for value in s:
                result += group[value]

            answer = max(result, answer)

print(answer)
