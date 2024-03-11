import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        stack.append(int(arr[1]))
        continue
    if arr[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
        continue
    if arr[0] == 'size':
        print(len(stack))
        continue
    if arr[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
        continue
    if arr[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        continue