import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[0], x[1]))

temp = [arr[0][1]]
for a, b in arr[1:]:
    if temp[0] <= a:
        heapq.heappop(temp)
    heapq.heappush(temp, b)

print(len(temp))