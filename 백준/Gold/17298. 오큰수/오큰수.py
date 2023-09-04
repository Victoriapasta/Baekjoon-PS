import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
NGE = [-1 for i in range(n)]
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i)

for i in NGE:
    print(i, end=' ')