n = int(input())
answer = 0

dp = [0 for i in range(11)]
dp[1] = 0
dp[2] = 1
dp[3] = 3
dp[4] = 6
dp[5] = 10
dp[6] = 15
dp[7] = 21
dp[8] = 28
dp[9] = 36
dp[10] = 45

print(dp[n])
