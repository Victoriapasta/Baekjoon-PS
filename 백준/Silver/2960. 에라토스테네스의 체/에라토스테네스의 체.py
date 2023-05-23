import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [True for i in range(n+1)]
ans = []
for i in range(2, n+1):
    if dp[i]:
        for j in range(i, n+1, i):
            if dp[j]:
                dp[j] = False
                ans.append(j)

print(ans[k-1])