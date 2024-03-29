import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n, m, k = map(int, input().split())
graph = [[] for i in range(n+1)]
dist = [[INF]*k for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(n):
    que = []
    heapq.heappush(que, (n, 0))
    dist[n][0] = 0

    while que:
        node, cost = heapq.heappop(que)

        for newnode, newcost in graph[node]:
            temp = cost + newcost
            if temp < dist[newnode][k-1]:
                dist[newnode][k-1] = temp
                dist[newnode].sort()
                heapq.heappush(que, (newnode, temp))

dijkstra(1)

for i in range(1, n+1):
    if dist[i][k-1] >= 1000000:
        print(-1)
    else:
        print(dist[i][k-1])