import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = []

for i in range(n):
    if not arr[i]:
        answer.append(i + 1)
        continue
    answer.insert(len(answer) - arr[i], i + 1)

print(*answer)