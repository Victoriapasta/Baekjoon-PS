import sys

input = sys.stdin.readline

t = int(input())

if t % 10:
    print(-1)
    exit(0)

buttons = [0, 0, 0]
while t:
    if t - 300 >= 0:
        t -= 300
        buttons[0] += 1
    elif t - 60 >= 0:
        t -= 60
        buttons[1] += 1
    else:
        t -= 10
        buttons[2] += 1

print(*buttons)