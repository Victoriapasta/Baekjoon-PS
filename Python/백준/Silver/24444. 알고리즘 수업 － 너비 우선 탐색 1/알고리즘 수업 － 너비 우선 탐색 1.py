import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for gr in graph:
    gr.sort()

visited = [False] * (n + 1)
start = 1
que = deque([r])
arrived = [0 for _ in range(n + 1)]
arrived[r] = 1
visited[r] = True

while que:
    nodeNumber = que.popleft()
    for node in graph[nodeNumber]:
        if not visited[node]:
            start += 1
            que.append(node)
            visited[node] = True
            arrived[node] = start

for ans in arrived[1:]:
    print(ans)