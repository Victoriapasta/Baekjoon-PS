import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(str(input().rstrip()))

s = ''
answer = 0
for i in range(m):
    temp = [0, 0, 0, 0] # A, C, G, T
    for j in range(n):
        if arr[j][i] == 'A':
            temp[0] += 1
        if arr[j][i] == 'C':
            temp[1] += 1
        if arr[j][i] == 'G':
            temp[2] += 1
        if arr[j][i] == 'T':
            temp[3] += 1

    if temp.index(max(temp)) == 0:
        newS = 'A'
    if temp.index(max(temp)) == 1:
        newS = 'C'
    if temp.index(max(temp)) == 2:
        newS = 'G'
    if temp.index(max(temp)) == 3:
        newS = 'T'

    s += newS

for i in range(n):
    for j in range(m):
        if s[j] != arr[i][j]:
            answer += 1

print(s)
print(answer)