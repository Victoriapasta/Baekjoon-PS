import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [-1001 for _ in range(n + 1)]
    arr = list(map(int, input().split()))

    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    if n == 1:
        print(dp[0])
    else:
        print(max(dp))
