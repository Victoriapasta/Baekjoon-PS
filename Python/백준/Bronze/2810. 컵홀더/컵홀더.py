import sys
input = sys.stdin.readline

n = int(input())

chairs = str(input().rstrip())
st = '*'
answer = 0

for i in chairs:
    if i == 'S':
        st += 'S*'
    if i == 'L':
        if st[-1] == 'L':
            st += 'L*'
        else:
            st += 'L'

for i in st:
    if i == '*':
        answer += 1

print(min(answer, n))