def A(H):
    return H * 1.05


def B(H):
    return H * 1.20


def C(H):
    return H * 1.35


if __name__ == '__main__':
    h, n = map(int, input().split())

    dp = [h for i in range(n + 1)]

    for i in range(1, n + 1):
        if i >= 5:
            dp[i] = max(A(dp[i - 1]), B(dp[i - 3]), C(dp[i - 5]))
        elif i >= 3:
            dp[i] = max(A(dp[i - 1]), B(dp[i - 3]))
        else:
            dp[i] = A(dp[i - 1])
        dp[i] = int(dp[i])

    print(int(dp[n]))
