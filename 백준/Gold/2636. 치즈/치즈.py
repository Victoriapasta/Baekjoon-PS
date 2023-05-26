import sys
input = sys.stdin.readline
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    que = deque([(0, 0)])
    visited = [[False for _ in range(m)] for __ in range(n)]
    visited[0][0] = True
    cnt = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if n > nx >= 0 and m > ny >= 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    cnt += 1
                    continue
                else:
                    que.append((nx, ny))

    return cnt

t = 0
while True:
    temp = bfs()
    if temp:
        a = temp
    else:
        break
    t += 1

print(t)
print(a)