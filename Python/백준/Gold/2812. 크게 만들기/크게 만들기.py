import sys
input = sys.stdin.readline

n, k = map(int, input().split())

sentence = str(input().rstrip())
stack = []
for num in sentence:
    if not stack:
        stack.append(num)
        continue

    if stack[-1] < num and k:
        while stack and stack[-1] < num and k:
            stack.pop()
            k -= 1
        stack.append(num)
    else:
        stack.append(num)

if k:
    while k:
        stack.remove(min(stack))
        k -= 1
print(*stack, sep='')