import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
que = deque()
for i in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        que.append(int(arr[1]))
        continue
    if arr[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
        continue
    if arr[0] == 'size':
        print(len(que))
        continue
    if arr[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
        continue
    if arr[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
        continue
    if arr[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
