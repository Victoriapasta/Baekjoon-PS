import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp = i + j
        if temp >= n:
            break

        if i == 0:
            dp[j][temp] = 1
            continue

        if i == 1 and arr[j] == arr[temp]:
            dp[j][temp] = 1
            continue

        if arr[j] == arr[temp] and dp[j + 1][temp - 1]:
            dp[j][temp] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
