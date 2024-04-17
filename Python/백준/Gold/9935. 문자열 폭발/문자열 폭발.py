import sys

input = sys.stdin.readline

sentence = str(input().rstrip())
bomb = str(input().rstrip())


stack = []

for word in sentence:
    stack.append(word)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
