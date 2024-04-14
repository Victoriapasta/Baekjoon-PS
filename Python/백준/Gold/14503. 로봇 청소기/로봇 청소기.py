import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]  # 0 -> 북, 1 -> 동, 2 -> 남, 3 -> 서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = []
visited = [[False for _ in range(m)] for __ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
x, y, dir = r, c, d
dirty = False

while True:
    if graph[x][y] == 0:
        answer += 1
        graph[x][y] = 2

    dirty = False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:  # 청소할 곳이 주변에 있으면
            dirty = True
            break

    if dirty:
        dir = (dir + 3) % 4  # 반시계 90도
        nx, ny = x + dx[dir], y + dy[dir]
        if graph[nx][ny] == 0:
            x, y = nx, ny
    else:
        rdir = (dir + 2) % 4  # 뒤로
        rx, ry = x + dx[rdir], y + dy[rdir]  # 후진
        if graph[rx][ry] == 1:  # 후진못할때
            print(answer)
            exit(0)
        else:
            x, y = rx, ry

