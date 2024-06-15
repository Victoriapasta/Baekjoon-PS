import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]
minn = arr[0]
for i in range(1, n):
    minn = min(minn, arr[i])
    dp.append(max(dp[i-1], arr[i] - minn))

print(*dp)