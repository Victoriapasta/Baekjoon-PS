import sys

input = sys.stdin.readline

t = str(input().rstrip())
p = str(input().rstrip())
cnt = 0

while True:
    index = t.find(p)
    if index == -1:
        break

    cnt += 1
    t = t[index + len(p):]

print(cnt)
