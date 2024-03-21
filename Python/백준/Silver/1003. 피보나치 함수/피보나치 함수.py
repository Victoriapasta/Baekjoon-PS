t = int(input())

for i in range(t):
    n = int(input())
    dp = [0, 1, 1]
    if n == 0:
        print(1, 0)
        continue
    if n == 1:
        print(0, 1)
        continue
    for j in range(2, n):
        dp.append(dp[j - 1] + dp[j])

    print(dp[-2], dp[-1])
