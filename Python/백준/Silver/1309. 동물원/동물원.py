n = int(input())

dp = [7 for _ in range(n + 1)]
dp[1] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[-1])