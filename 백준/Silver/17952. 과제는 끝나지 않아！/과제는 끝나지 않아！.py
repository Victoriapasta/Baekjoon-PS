import sys
input = sys.stdin.readline

t = int(input())
stack = []
summ = 0
for i in range(t):
    arr = list(map(int, input().split()))
    if arr[0]:
        stack.append(arr)

    if stack:
        stack[-1][2] -= 1
        if not stack[-1][2]:
            summ += stack[-1][1]
            stack.pop()

print(summ)
