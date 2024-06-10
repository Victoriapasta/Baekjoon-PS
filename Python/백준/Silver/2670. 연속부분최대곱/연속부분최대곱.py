import sys

input = sys.stdin.readline

n = int(input())
arr = []
dp = [0 for i in range(n + 1)]
for _ in range(n):
    arr.append(float(input()))

dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] * arr[i], arr[i])

print('%.3f' % max(dp))
