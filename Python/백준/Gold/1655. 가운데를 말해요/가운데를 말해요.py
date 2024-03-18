import heapq
import sys
input = sys.stdin.readline

n = int(input())

minheap = []
maxheap = []

for i in range(n):
    number = int(input())

    if not maxheap:
        heapq.heappush(maxheap, -number)
        print(-maxheap[0])
        continue

    if len(maxheap) <= len(minheap):
        heapq.heappush(maxheap, -number)
    else:
        heapq.heappush(minheap, number)

    if -maxheap[0] > minheap[0]:
        maxtmp = -heapq.heappop(maxheap)
        mintmp = heapq.heappop(minheap)
        heapq.heappush(maxheap, -mintmp)
        heapq.heappush(minheap, maxtmp)

    print(-maxheap[0])
