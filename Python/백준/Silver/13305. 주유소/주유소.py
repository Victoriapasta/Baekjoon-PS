import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

temp = cost[0]
dp = [0 for _ in range(n-1)]
dp[0] = cost[0] * dist[0]
for i in range(1, n-1):
    if cost[i] < temp:
        temp = cost[i]
    dp[i] = temp * dist[i] + dp[i-1]

print(dp[-1])
