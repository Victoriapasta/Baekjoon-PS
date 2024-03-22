import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
if n == 1:
    print(arr[0])
    exit(0)
    
dp = [[0, 0] for _ in range(n)] # 0번째 인덱스는 1칸, 1번째 인덱스는 2칸 이동

dp[0][0] = arr[0]
dp[0][1] = arr[0]
dp[1][1] = arr[1]
dp[1][0] = dp[0][0] + arr[1]

for i in range(2, n):
    dp[i][0] = arr[i] + dp[i-1][1]
    dp[i][1] = max(dp[i-2][1], dp[i-2][0]) + arr[i]

print(max(dp[-1]))