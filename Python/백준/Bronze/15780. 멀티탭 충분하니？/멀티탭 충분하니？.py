import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for tap in arr:
    if not tap % 2:
        answer += tap // 2
        continue
    if tap % 2:
        answer += tap // 2 + 1
        continue

if answer >= n:
    print('YES')
else:
    print('NO')