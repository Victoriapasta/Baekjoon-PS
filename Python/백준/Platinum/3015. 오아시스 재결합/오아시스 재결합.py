import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

stack = []
cnt = 0

for i in range(n):

    if not stack or stack[-1][0] > arr[i]:
        stack.append([arr[i], 1]) # stack[index][0]은 키 stack[index][1]은 그 키를 가진 사람 수
    elif stack[-1][0] == arr[i]:
        cnt += stack[-1][1]
        stack[-1][1] += 1
    else:
        while stack and stack[-1][0] < arr[i]: # stack이 있고 키가 크면 계속 삭제
            cnt += stack.pop()[-1]

        if stack and arr[i] == stack[-1][0]:
            cnt += stack[-1][1]
            stack[-1][1] += 1
        else:
            stack.append([arr[i], 1])

    if len(stack) >= 2:
        cnt += 1

print(cnt)
