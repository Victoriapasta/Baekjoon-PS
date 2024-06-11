import sys
input = sys.stdin.readline

while True:
    s = str(input().rstrip())
    if s == 'END':
        break

    answer = ''
    for char in reversed(s):
        answer += char

    print(answer)