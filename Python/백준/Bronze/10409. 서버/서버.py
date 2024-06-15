import sys

input = sys.stdin.readline

n, t = map(int, input().split())

arr = list(map(int, input().split()))
temp = 0
answer = 0
for time in arr:
    if temp > t:
        break
    temp += time
    answer += 1

if temp > t:
    print(answer - 1)
else:
    print(answer)
