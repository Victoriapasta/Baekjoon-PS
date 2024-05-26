import sys

dx = [-1, 0, 1]
dy = [-1, -1, -1]

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
visited = [[False for _ in range(c)] for __ in range(r)]

for i in range(r):
    graph.append(list(map(str, input().rstrip())))

answer = 0


def dfs(x, y):
    global answer
    if y == 0:
        answer += 1
        return True

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False


for i in range(r):
    dfs(i, c - 1)

print(answer)
