import sys

input = sys.stdin.readline

n = int(input())
sequence = []
stack = []
startNum = 1

for i in range(n):
    element = int(input())
    while startNum <= element:
        stack.append('+')
        sequence.append(startNum)
        startNum += 1

    if element == sequence[-1]:
        stack.append('-')
        sequence.pop()
    else:
        print("NO")
        exit(0)

print('\n'.join(stack))
