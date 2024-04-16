import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

graph = []
visited = [[False for _ in range(m)] for __ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

maxmax = 0

for row in graph:
    maxmax = max(maxmax, max(row))

answer = 0


def backTracking(x, y, dist, score):
    global answer

    if dist == 4:
        answer = max(answer, score)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if dist == 2:
                visited[nx][ny] = True
                backTracking(x, y, dist + 1, score + graph[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            backTracking(nx, ny, dist + 1, score + graph[nx][ny])
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        backTracking(i, j, 1, graph[i][j])
        visited[i][j] = False

print(answer)
