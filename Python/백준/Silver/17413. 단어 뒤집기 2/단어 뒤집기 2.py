import sys

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
answer = []
stack = []
tag = False

for char in arr:
    if char == '<':
        while stack:
            answer.append(stack.pop())
        tag = True
        answer.append(char)
        continue

    if char == '>':
        tag = False
        answer.append(char)
        continue

    if not tag:
        if char != ' ':
            stack.append(char)
            continue
        if char == ' ':
            while stack:
                answer.append(stack.pop())
            answer.append(' ')

    if tag:
        answer.append(char)
        continue

while stack:
    answer.append(stack.pop())
print(''.join(answer))
