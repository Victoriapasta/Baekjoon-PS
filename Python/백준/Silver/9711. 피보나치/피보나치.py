import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 10001
dp[1] = 1
dp[2] = 1

for i in range(3, 10001):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(n):
    n, m = map(int, input().split())
    print('Case #{}: {}'.format(_ + 1, dp[n] % m))