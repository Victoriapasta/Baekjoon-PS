import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
que = list(map(int, input().split()))

heapq.heapify(que)

for i in range(m):
    min1 = heapq.heappop(que)
    min2 = heapq.heappop(que)
    temp = min1 + min2
    heapq.heappush(que, temp)
    heapq.heappush(que, temp)

print(sum(que))
