import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

state = 0
answer = 0

for milk in arr:
    if milk == state % 3:
        answer += 1
        state += 1

print(answer)