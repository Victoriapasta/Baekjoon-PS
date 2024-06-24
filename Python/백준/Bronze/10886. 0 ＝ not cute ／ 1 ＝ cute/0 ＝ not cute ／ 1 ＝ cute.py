n = int(input())
dp = {}

for i in range(n):
    a = int(input())
    if a not in dp:
        dp[a] = 1
    else:
        dp[a] += 1

if n == 1:
    if a == 1:
        print('Junhee is cute!')
    else:
        print('Junhee is not cute!')
else:
    if dp[0] > dp[1]:
        print('Junhee is not cute!')
    else:
        print('Junhee is cute!')