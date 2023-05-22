import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maps = [[] for _ in range(n+1)]
dist = [0 for i in range(n+1)]
answer = []
for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    dist[b] += 1

def topologySort():
    que = deque([])
    for i in range(1, n+1):
        if not dist[i]:
            que.append(i)

    for i in range(n):
        if not que:
            return
        node = que.popleft()
        for nextnode in maps[node]:
            dist[nextnode] -= 1
            if not dist[nextnode]:
                que.append(nextnode)

        answer.append(node)


topologySort()

print(*answer)
