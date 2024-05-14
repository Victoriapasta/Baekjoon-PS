import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
bags = []
for _ in range(n):
    mi, vi = map(int, input().split())
    heapq.heappush(bags, [mi, vi])

c = []
for _ in range(k):
    c.append(int(input()))

c.sort()
tempbag = []
for w in c:
    while bags and bags[0][0] <= w:
        heapq.heappush(tempbag, -heapq.heappop(bags)[1])
    if tempbag:
        answer -= heapq.heappop(tempbag)
    elif not bags:
        break

print(answer)
