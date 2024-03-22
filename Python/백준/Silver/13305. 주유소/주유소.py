import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

totalDist = sum(dist)

dp = [totalDist * cost[0] for _ in range(n-1)]
temp = 0

for i in range(1, n-1):
    totalDist -= dist[i - 1]
    temp += cost[i-1] * dist[i-1]
    dp[i] = temp + cost[i] * totalDist

print(min(dp))
