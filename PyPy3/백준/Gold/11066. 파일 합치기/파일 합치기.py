import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0 for __ in range(n + 1)] for ___ in range(n + 1)]

    suf = [0 for __ in range(n + 1)]
    for i in range(1, n + 1):
        suf[i] = suf[i - 1] + arr[i]

    for i in range(2, n + 1):
        for j in range(1, n + 2 - i):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + suf[i + j - 1] - suf[j - 1]

    print(dp[1][n])
